from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk ()
GUI.title ('โปรแกรมบันทึกรายรับรายจ่าย')
GUI.geometry('500x500')

L1 =Label(GUI,text='บันทึกรายรับรายจ่ายประจำวัน',font=('sukhumvit',30),fg='green')
L1.place(x=25,y=50)

###################################

L2 = Label(GUI,text='วันที่',font=('sukhumvit',20),fg='black')
L2.place(x=60,y=130)
E2 = ttk.Entry()#input ข้อมูล
E2.place(x=160,y=130)




L3 = Label(GUI,text='หมวดหมู่',font=('sukhumvit',20),fg='black')
L3.place(x=60,y=180)
combo1=ttk.Combobox(value=["รายรับ","รายจ่าย"])
combo1.place(x=160,y=180)



L4 = Label(GUI,text='รายการ',font=('sukhumvit',20),fg='black')
L4.place(x=60,y=230)
E4 = ttk.Entry()#input ข้อมูล
E4.place(x=160,y=230)



L5 = Label(GUI,text='จำนวนเงิน',font=('sukhumvit',19),fg='black')
L5.place(x=60,y=280)
L6 = Label(GUI,text='บาท',font=('sukhumvit',20),fg='black')
L6.place(x=300,y=280)

E5 = ttk.Entry()#input ข้อมูล
E5.place(x=160,y=290)


#############################
def Button ():
    text = 'บันทึกข้อมูลสำเร็จ'
    messagebox.showinfo('บันทึก',text)

B1 = ttk.Button(text='บันทึก',command=Button)
B1.place(x=220,y=350)
























