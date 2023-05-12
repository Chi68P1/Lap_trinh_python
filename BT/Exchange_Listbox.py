from tkinter import *

W = Tk()
W.geometry("450x400+900+100")
W.title("MONEY EXCHANGE")


def B1_click():
    if E1.get() == '':
        m = 0
    else:
        m =float(E1.get())
        x = LB.curselection()
    if len(x)== 0:
        L1.configure(text="Mời lựa chọn mệnh giá")
    else:

        if x[0] == 0:  #x[0] là sự lựa chọn đầu tiên
            A = m*22000
            L2.configure(text="USD")
        elif x[0] == 1:
            A = m*26000
            L2.configure(text="EURO")
        elif x[0] == 2:
            A = m*200
            L2.configure(text="JYP")
        L1.configure(text='GIÁ TRỊ QUY ĐỔI: {:,} VND'.format(A))
	

B = ["USD: 22.000","EUR: 26.000",'JYP: 200']
C = StringVar(value = B)
LB= Listbox(master = W, font=("arial",15),width = 13,height = 6,listvariable = C, selectmode =EXTENDED)
LB.place(x=50,y=80)

E1 = Entry(master = W, font =("arial",15),width = 8 )
E1.place(x=250,y=80)

B1 = Button(master = W, text ='EXCHANGE', font = ('arial',15),width = 10,command = B1_click) 
B1.place(x=250,y=160)

L1 = Label(master = W, text = "GIÁ TRỊ QUY ĐỔI:   VND", font = ("arial",15),fg ="blue") #italic: in nghiêng
L1.place(x=120,y=260)
L2 = Label(master = W, text = "", font = ("arial",15),fg ="blue") 
L2.place(x=350,y=80)



W.mainloop()