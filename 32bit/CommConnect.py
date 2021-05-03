from pykiwoom.kiwoom import *
import pandas as pd

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")

name = kiwoom.GetMasterCodeName("005930")
print(name)

df  = kiwoom.block_request("opt10001",
                          종목코드="005930",
                          output="주식기본정보",
                          next=0)
df.to_csv('SamsungElectronics_StockBasicInformation.csv', index=False, encoding='cp949')