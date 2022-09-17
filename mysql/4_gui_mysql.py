# GUI를 활용한 데이터 입력 조회

import pymysql
from tkinter import *

def insertData():
    conn, cur = None, None
    data = ['' for _ in range(4)]
    sql = ''
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000', db='solodb', charset='utf8')
    cur = conn.cursor()
    
    data[0] = edt1.get()
    data[1] = edt2.get()
    data[2] = edt3.get()
    data[3] = edt4.get()
    
    sql = f"INSERT INTO userTable VALUES('{data[0]}', '{data[1]}', '{data[2]}', {data[3]})"
    cur.execute(sql)
    conn.commit()
    conn.close()
    
def selectData():
    data1, data2, data3, data4 = [], [], [], []
    sql = ''
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000', db='solodb', charset='utf8')
    cur = conn.cursor()
    
    sql = f"SELECT * FROM userTable"
    cur.execute(sql)
    
    while True:
        row = cur.fetchone()
        if row == None:
            break
        data1.append(row[0]); data2.append(row[1]); data3.append(row[2]); data4.append(row[3])
        
    listData1.delete(0, listData1.size()-1); listData2.delete(0, listData2.size()-1)
    listData3.delete(0, listData3.size()-1); listData4.delete(0, listData4.size()-1)
    
    for i1, i2, i3, i4 in zip(data1, data2, data3, data4):
        listData1.insert(END, i1); listData2.insert(END, i2)
        listData3.insert(END, i3); listData4.insert(END, i4)
        
    conn.close()
    

root = Tk()
root.geometry('700x300')
root.title('완전한 GUI 프로그래밍')
root.resizable(False, False)

edtFrame = Frame(root)
edtFrame.pack()
listFrame = Frame(root)
listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

label1 = Label(edtFrame, width=5, text='ID')
label1.pack(side=LEFT)
edt1 = Entry(edtFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(edtFrame, width=5, text='Name')
label2.pack(side=LEFT)
edt2 = Entry(edtFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(edtFrame, width=5, text='Email')
label3.pack(side=LEFT)
edt3= Entry(edtFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(edtFrame, width=5, text='Year')
label4.pack(side=LEFT)
edt4 = Entry(edtFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text='입력', command=insertData)
btnInsert.pack(side=LEFT, padx=5, pady=10)
btnInsert2 = Button(edtFrame, text='조회', command=selectData)
btnInsert2.pack(side=LEFT, padx=5, pady=10)

listData1 = Listbox(listFrame, bg='yellowgreen')
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg='#888888')
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg='yellow')
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg='#AA00AA')
listData4.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()