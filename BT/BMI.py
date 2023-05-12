from tkinter import *
from PIL import Image,ImageTk

W = Tk()
W.geometry("555x500+950+100")
W.title("BMI")

def B1_click():
	x1= float(E1.get())
	x2= float(E2.get())
	BMI= round(x2/(x1*x1),1)
	KQ.configure(text ="BMI =" + str(BMI))
	if BMI < 18.5:
		KQ1.configure(text = "Gầy")
	elif 18.5<=BMI<25:
		KQ1.configure(text = "Bình thường")
	elif 25<=BMI<=30:
		KQ1.configure(text = "Thừa cân")
	else:
		KQ1.configure(text = "Béo phì")

L1 = Label(master = W, text = "Adult BMI Caculator", font = ("arial",20),bg = "blue",fg ="white") #italic: in nghiêng
L1.place(x=0,y=0,width=550)
L2 = Label(master = W, text = "Chiều cao: (m)", font = ("arial",15,"bold",'italic')) #italic: in nghiêng
L2.place(x=50,y=100,width=250,heigh=20)
L3 = Label(master = W, text = "Cân nặng: (kg)", font = ("arial",15,"bold",'italic')) 
L3.place(x=50,y=250,width=250,heigh=20)

KQ = Label(master = W, text = "", font = ("arial",20)) 
KQ.place(x=300,y=200,width=200,heigh=20)
KQ1 = Label(master = W, text = "", font = ("arial",20)) 
KQ1.place(x=300,y=300,width=200,heigh=30)

E1 = Entry(master = W, font =("arial",15),width = 10 )
E1.place(x=70,y=150,width=150,heigh=50)
E2 = Entry(master = W, font =("arial",15),width = 10 )
E2.place(x=70,y=300,width=150,heigh=50)

B1 = Button(master = W, text ='Caculate', font = ('arial',15),heigh= 3,width= 12,bg = "blue",fg = "white",command = B1_click)
B1.place(x=70,y=370,width=150,heigh=50)

W.mainloop()