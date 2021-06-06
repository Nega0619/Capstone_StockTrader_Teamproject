from tkinter import *
from tkinter import filedialog
import main
import numpy as np

if __name__ == '__main__':

    #path=load_gui()
    #Image=readImage(path)

    root = Tk()
    root.title("주식 강화학습기")
    root.geometry("640x480")
    root.resizable(FALSE,FALSE)

    file_frame=LabelFrame(root)
    file_frame.pack()

    explainFolder=Label(file_frame, text="CSV파일 위치 = ")
    explainFolder.pack(side="left")

    entry=Entry(file_frame, width=40)
    entry.pack(side="left")

    def getCSV():
        files = filedialog.askopenfilename(title="학습시킬 데이터 CSV파일을 선택하세요.", \
                                           filetypes=(("CSV 파일", "*.csv"),("모든 파일", "*.*")),\
                                           initialdir="C:/Users/920/Documents/GitHub/Capstone_StockTrader_Teamproject/64bit\data/v2")
        #print(files)
        entry.insert(END,files) # 다시 클릭해서 추가하면 파일 경로가 이어진다...

    btn_getCsv = Button(file_frame, text="찾아보기", command=getCSV)
    btn_getCsv.pack(side="right")

    def handle_startdate_click(event):
        e_startdate.delete(0,"end")

    def handle_enddate_click(event):
        e_enddate.delete(0,"end")

    def handle_balance_click(event):
        e_balance.delete(0,"end")

    e_startdate = Entry(root, width=30)
    e_startdate.pack()
    e_startdate.insert(END,"시작 날짜를 입력하세요")
    e_startdate.bind("<1>", handle_startdate_click)

    e_enddate = Entry(root, width=30)
    e_enddate.pack()
    e_enddate.insert(END, "종료 날짜를 입력하세요")
    e_enddate.bind("<1>", handle_enddate_click)

    e_balance = Entry(root, width=30)
    e_balance.pack()
    e_balance.insert(END, "시작 자본금을 입력하세요")
    e_balance.bind("<1>", handle_balance_click)

    def get_entrydata():
        e_startdate.get() #엔트리에 있는 값을 가져온다
        e_enddate.get()
        e_balance.get()

        
    #btn_learn = Button(root, text="학습하기", command=main.main()) # 오류가 떠서 일단 주석 처리함

    root.mainloop()