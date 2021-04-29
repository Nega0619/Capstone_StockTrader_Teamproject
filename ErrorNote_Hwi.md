# 사용할 종목코드

- 삼성전자 우선주 005935
- 카카오 035720



# 환경 설명



## 개발 환경

Python 3.7.6 32 bit - IDE	(kiwoom open api가 32bit 파이썬을 필요로함)

Python 3.7.6 64 bit - IDE	(RLtrader에서는 64bit 필요로함.)



아나콘다 5.3.0 64bit -> 32 비트 설치. 파이참에서 인터프리터 할당.

Python IDE 3.7.9 64bit -> 파이참에서 인터프리터 할당



https://repo.anaconda.com/archive/



## 필요 패키지 목록

설치 방법 cmd창에 (pip install numpy==1.18.1)



## 64bit

Numpy 1.18.1 

pandas 1.0.1

matplotlib 3.1.3

keras 2.2.4

tensorflow 1.15	

(파이썬 3.8버전 이상에서는 안돌아가므로 꼭 3.8미만으로 설치, python 64bit 이상이여야 함.)

plaidml-keras 0.6.2



## 32bit

pyqt5==5.12.1

pyqtwebengine==5.12.1

pykiwoom



## 참고 사이트

- 퀀트투자를위한 키움 OpenAPI 사용법

  https://wikidocs.net/77481



# 버전처리를 받으시려면 현재 실행중인 OpenAPI OCX ~~

![image-20210429143348200](C:\Users\gleyd\AppData\Roaming\Typora\typora-user-images\image-20210429143348200.png)



C:\openAPI에서  `opversionup.exe` 실행 후 다시 실행



# csv 파일 만들기



## 웹크롤링 - 종목코드 가져오기

https://lifeonroom.com/study-lab/get-stock-code-price/



## 코딩으로

https://m.blog.naver.com/PostView.nhn?blogId=whdghk414141&logNo=221105259323&proxyReferer=https:%2F%2Fwww.google.com%2F



- 파이썬 pandas에서 csv파일쓰는 방법
- https://wikidocs.net/43280