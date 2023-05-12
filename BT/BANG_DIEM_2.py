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
            E1.delete(0,END)      
            E2.delete(0,END) 
            messagebox.showinfo(title="Thông báo", message= "Mời nhập lại giá trị")
   

def B2_click():
    x = LB1.curselection()
    if len(x) == 0:
        pass
    else:
        LB1.delete(x)
        LB2.delete(x)

def Max_Min():
    ma = 0
    mi = 0
    a=LB2.get(0,"end")
    b = list(a)
    for i in range(0,len(b)):
        b[i] = int(b[i])
    ma = max(b)
    mi = min(b)
    
    messagebox.showinfo(title="Thông báo", message= "Điểm lớn nhất là {}, nhỏ nhất là {}".format(ma,mi) )

def Delete_All():
    M1 = messagebox.askyesno(title= "Thông báo", message= "Bạn có muốn xóa toàn bộ?")
    if M1 == True:
        LB1.delete(0,END)
        LB2.delete(0,END)
        E1.delete(0,END)
        E2.delete(0,END)
    else:
        pass
def exit():
    M1 = messagebox.askyesno(title = "Thông báo",message = "Bạn có muốn thoát chương trình")
    if M1 == True:
        W.destroy()

B1 = Button(master=W,text="ADD",font=("arial",15),width=12,bg="white",fg="black", command=B1_click)
B1.place(x=500,y=150)
B2 = Button(master=W,text="DELETE",font=("arial",15),width=12,bg="white",fg="black",command=B2_click)
B2.place(x=500,y=200)

LB1 = Listbox(master=W,font=("arial",15),width=15,height=10,selectmode=SINGLE)
LB1.place(x=20,y=110)
LB2 = Listbox(master=W,font=("arial",15),width=15,height=10)
LB2.place(x=250,y=110)

thanh_menu = Menu(master = W)
W.configure(menu = thanh_menu)

file_menu = Menu(master=thanh_menu, tearoff = False)
thanh_menu.add_cascade(label = "File", menu = file_menu)

file_menu.add_command(label = "Stats", command = Max_Min)
file_menu.add_command(label = "Delete All", command = Delete_All)
file_menu.add_command(label = "Exit", command = exit)

W.mainloop()