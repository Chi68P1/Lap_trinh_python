from tkinter import *
W = Tk()
W.geometry("450x400+900+100")
W.title("MONEY EXCHANGE")

x1= IntVar(value =0)

def B1_click():
	if E1.get()=="":
		L1.configure(text ="MỜI BẠN NHẬP GIÁ TRỊ")
	else:
		if int(E1.get())>=0:
			if x1.get() == 0:
				L1.configure(text ="CHƯA CHỌN LOẠI NGOẠI TỆ")
			else:
				a = float(E1.get())
				EX = x1.get()*a
				L1.configure(text ="GIÁ TRỊ QUY ĐỔI: {:,} VND".format(EX))

		else:
			L1.configure(text ="MỜI NHẬP LẠI")
	



C1 = Radiobutton(master = W,text = "USD: 22.000",font = ("arial",15),value = 22000,variable = x1)
C1.place(x=50,y=50)

C2 = Radiobutton(master = W,text = "EUR: 26.000",font = ("arial",15),value = 26000,variable = x1)
C2.place(x=50,y=120)
C3 = Radiobutton(master = W,text = "JYP: 200",font = ("arial",15),value = 200,variable = x1)
C3.place(x=50,y=190)

E1 = Entry(master = W, font =("arial",15),width = 12 )
E1.place(x=250,y=80)

B1 = Button(master = W, text ='EXCHANGE', font = ('arial',15),width = 10,command = B1_click) 
B1.place(x=250,y=160)

L1 = Label(master = W, text = "GIÁ TRỊ QUY ĐỔI:   VND", font = ("arial",15),fg ="blue") #italic: in nghiêng
L1.place(x=100,y=260)


W.mainloop()