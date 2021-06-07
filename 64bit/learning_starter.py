import os
import sys
import logging
import argparse
import json

import settings
import utils
import data_manager


def start_learning(test):
    print(test)
    stock_code = '005930'
    ver='v2'
    rl_method='a2c'
    net ='lstm'
    num_steps=5
    lr = 0.001
    discount_factor=0.9
    start_epsilon =1
    balance=10000000
    num_epoches = 300
    delayed_reward_threshold=0.1
    backend='tensorflow'
    #output_name = 'c_005930'
    output_name=utils.get_time_str()
    value_network_name=None
    policy_network_name = None
    reuse_models=False
    learning=True
    start_date='20170101'
    end_date='20171231'

    if backend == 'tensorflow':
        os.environ['KERAS_BACKEND'] = 'tensorflow'

    # 출력 경로 설정
    output_path = os.path.join(settings.BASE_DIR,
                               'output/{}_{}_{}'.format(output_name, rl_method, net))
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    # 파라미터 기록
    '''
    with open(os.path.join(output_path, 'params.json'), 'w') as f:
        f.write(json.dumps(vars(args)))'''

    # 로그 기록 설정
    file_handler = logging.FileHandler(filename=os.path.join(
        output_path, "{}.log".format(output_name)), encoding='utf-8')
    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.INFO)
    logging.basicConfig(format="%(message)s",
                        handlers=[file_handler, stream_handler], level=logging.DEBUG)

    # 로그, Keras Backend 설정을 먼저하고 RLTrader 모듈들을 이후에 임포트해야 함
    from agent import Agent
    from learners import ReinforcementLearner, DQNLearner, \
        PolicyGradientLearner, ActorCriticLearner, A2CLearner, A3CLearner

    # 모델 경로 준비
    value_network_path = ''
    policy_network_path = ''
    if value_network_name is not None:
        value_network_path = os.path.join(settings.BASE_DIR,
                                          'models/{}.h5'.format(value_network_name))
    else:
        value_network_path = os.path.join(
            output_path, '{}_{}_value_{}.h5'.format(
                rl_method, net, output_name))
    if policy_network_name is not None:
        policy_network_path = os.path.join(settings.BASE_DIR,
                                           'models/{}.h5'.format(policy_network_name))
    else:
        policy_network_path = os.path.join(
            output_path, '{}_{}_policy_{}.h5'.format(
                rl_method, net, output_name))

    common_params = {}
    list_stock_code = []
    list_chart_data = []
    list_training_data = []
    list_min_trading_unit = []
    list_max_trading_unit = []

    if (stock_code != None):
        # 차트 데이터, 학습 데이터 준비
        chart_data, training_data = data_manager.load_data(
            os.path.join(settings.BASE_DIR,
                         'data/{}/{}.csv'.format(ver, stock_code)),
            start_date, end_date, ver=ver)

        # 최소/최대 투자 단위 설정
        min_trading_unit = max(int(100000 / chart_data.iloc[-1]['close']), 1)
        max_trading_unit = max(int(1000000 / chart_data.iloc[-1]['close']), 1)

        # 공통 파라미터 설정
        common_params = {'rl_method': rl_method,
                         'delayed_reward_threshold': delayed_reward_threshold,
                         'net': net, 'num_steps': num_steps, 'lr': lr,
                         'output_path': output_path, 'reuse_models': reuse_models}

        # 강화학습 시작
        learner = None
        if rl_method != 'a3c':
            common_params.update({'stock_code': stock_code,
                                  'chart_data': chart_data,
                                  'training_data': training_data,
                                  'min_trading_unit': min_trading_unit,
                                  'max_trading_unit': max_trading_unit})
            if rl_method == 'dqn':
                learner = DQNLearner(**{**common_params,
                                        'value_network_path': value_network_path})
            elif rl_method == 'pg':
                learner = PolicyGradientLearner(**{**common_params,
                                                   'policy_network_path': policy_network_path})
            elif rl_method == 'ac':
                learner = ActorCriticLearner(**{**common_params,
                                                'value_network_path': value_network_path,
                                                'policy_network_path': policy_network_path})
            elif rl_method == 'a2c':
                learner = A2CLearner(**{**common_params,
                                        'value_network_path': value_network_path,
                                        'policy_network_path': policy_network_path})
            elif rl_method == 'monkey':
                net = rl_method
                num_epoches = 1
                discount_factor = None
                start_epsilon = 1
                learning = False
                learner = ReinforcementLearner(**common_params)

            if learner is not None:
                learner.run(balance=balance,
                            num_epoches=num_epoches,
                            discount_factor=discount_factor,
                            start_epsilon=start_epsilon,
                            learning=learning)
                learner.save_models()
        else:
            list_stock_code.append(stock_code)
            list_chart_data.append(chart_data)
            list_training_data.append(training_data)
            list_min_trading_unit.append(min_trading_unit)
            list_max_trading_unit.append(max_trading_unit)

    if rl_method == 'a3c':
        learner = A3CLearner(**{
            **common_params,
            'list_stock_code': list_stock_code,
            'list_chart_data': list_chart_data,
            'list_training_data': list_training_data,
            'list_min_trading_unit': list_min_trading_unit,
            'list_max_trading_unit': list_max_trading_unit,
            'value_network_path': value_network_path,
            'policy_network_path': policy_network_path})

        learner.run(balance=balance, num_epoches=num_epoches,
                    discount_factor=discount_factor,
                    start_epsilon=start_epsilon,
                    learning=learning)
        learner.save_models()



if __name__ == '__main__':
    start_learning(3)

