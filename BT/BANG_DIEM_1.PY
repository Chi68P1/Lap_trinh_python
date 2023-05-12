from tkinter import *
from tkinter import messagebox

W = Tk()
W.geometry("700x500+800+150")
W.title("BẢNG ĐIỂM")


L1 = Label(master=W,font=("arial",15),text="HỌ VÀ TÊN: ",fg="blue")
L1.place(x=20,y=20)
L2 = Label(master=W,font=("arial",15),text="ĐIỂM SỐ: ",fg="blue")
L2.place(x=250,y=20)

E1 = Entry(master=W,font=("arial",15),width=15)
E1.place(x=20,y=60)
E2 = Entry(master=W,font=("arial",15),width=15)
E2.place(x=250,y=60)

def B1_click():

    if E1.get() == '' or E2.get() == '':
       pass
    else:

        try:
            val = float(E2.get())
            if float(E2.get()) > 10:
                LB1.insert(0,E1.get())
                E1.delete(0,END)
                LB2.insert(0,10)
                E2.delete(0,END)   
            elif float(E2.get()) < 0:
                LB1.insert(0,E1.get())
                E1.delete(0,END)
                LB2.insert(0,0)
                E2.delete(0,END)
            else:
                LB1.insert(0,E1.get())
                E1.delete(0,END)
                LB2.insert(0,E2.get())
                E2.delete(0,END)
        
        except ValueError:
            messagebox.showinfo(title="Thông báo", message= "Mời nhập lại giá trị")
    

def B2_click():
    x = LB1.curselection()
    if len(x) == 0:
        pass
    else:
        LB1.delete(x)
        LB2.delete(x)

B1 = Button(master=W,text="ADD",font=("arial",15),width=12,bg="white",fg="black", command=B1_click)
B1.place(x=500,y=150)
B2 = Button(master=W,text="DELETE",font=("arial",15),width=12,bg="white",fg="black",command=B2_click)
B2.place(x=500,y=200)

LB1 = Listbox(master=W,font=("arial",15),width=15,height=10,selectmode=SINGLE)
LB1.place(x=20,y=110)
LB2 = Listbox(master=W,font=("arial",15),width=15,height=10)
LB2.place(x=250,y=110)

W.mainloop()