from tkinter import *
W = Tk()
W.geometry("500x450+900+100")

x = IntVar()

W.title("BMI PRO")
L1 = Label(master = W,text = "CHIỀU CAO (cm) ",font = ("arial",12))
L1.place(x=50,y=50)
L2 = Label(master = W,text = "CÂN NẶNG (kg) ",font = ("arial",12))
L2.place(x=50,y=150)

L3 = Label(master = W,text = "BMI:  ",font = ("arial",12))
L3.place(x=200,y=300)

E1 =Entry(master = W,font = ("arial",12),width = 12)
E1.place(x=50,y=100,heigh= 30)
E2 =Entry(master = W,font = ("arial",12),width = 12)
E2.place(x=50,y=200,heigh= 30)

def R_click():
    if x.get()==0:
        L1.configure(text='CHIỀU CAO (cm):')
        L2.configure(text='CÂN NẶNG (kg):')
        a=E1.get()
    else:
        L1.configure(text='CHIỀU CAO (Inches):')
        L2.configure(text='CÂN NẶNG (Pounds):')

R1 = Radiobutton(master = W,text = "Vietnam",font = ("arial",12),value = 0,variable = x,command = R_click)
R1.place(x=250,y=50)
R2 = Radiobutton(master = W,text = "English",font = ("arial",12),value = 1,variable = x,command = R_click)
R2.place(x=250,y=100)

def B_click():
	if E1.get()=="" or E2.get()=="":
		L3.configure(text = "Mời nhập giá trị")
	else:
	    if x.get()==0:
	        a = float(E1.get())/100
	        b = float(E2.get())
	        BMI = round(b/(a*a),2)
	        L3.configure(text = 'BMI = '+ str(BMI))
	    else:
	        a = float(E1.get())
	        b = float(E2.get())
	        BMI = round(b/(a*a)*703,2)
	        L3.configure(text = 'BMI= '+ str(BMI))

B = Button(master = W,text = "CALCULATE",font = ("arial",12),command = B_click)
B.place(x=250,y=200)

W.mainloop()