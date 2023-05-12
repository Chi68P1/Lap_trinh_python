from tkinter import *
w = Tk()
w.geometry('480x380+500+100')
w.title('BMI CALCULATOR')
F1 = Frame(master =w,bg= "green")
F1.place(x=10,y=20,width =100)
F2 = Frame(w)
F2.place(x=240,y=40)
x = IntVar()


L1= Label(F1, text = 'CHIỀU CAO (cm):',font=('arial',14))
L1.grid(row=0,column=0,padx=30,pady=15,sticky = 'w')
E1 = Entry(master = F1, font =('arial',15), width = 12)
E1.grid(row=1,column=0,padx=30,sticky ='w')
L2= Label(master = F1, text = 'CÂN NẶNG (kg):',font=('arial',14))
L2.grid(row=2,column=0,padx=30,pady=15,sticky ='w')
E2 = Entry(master =F1,font =('arial',15), width = 12)
E2.grid(row=3,column=0,padx=30,sticky = 'w')

def R_click():
    if x.get()==0:
        L1.configure(text='CHIỀU CAO (cm):')
        L2.configure(text='CÂN NẶNG (kg):')
        a=E1.get()
    else:
        L1.configure(text='CHIỀU CAO (Inches):')
        L2.configure(text='CÂN NẶNG (Pounds):')

R1 = Radiobutton(master = F2,text = 'Metric',font=('arial',14),value =0,variable=x,command=R_click)
R1.grid(row=0,column=0,pady=20,sticky='w')
R2 = Radiobutton(master = F2,text = 'English',font=('arial',14),value=1,variable=x,command=R_click)
R2.grid(row=1,column=0,sticky='w')

def B_click():
    if x.get()==0:
        a = float(E1.get())/100
        b = float(E2.get())
        BMI = round(b/(a*a),2)
        L3.configure(text = 'BMI= '+ str(BMI))
    else:
        a = float(E1.get())
        b = float(E2.get())
        BMI = round(b/(a*a)*703,2)
        L3.configure(text = 'BMI= '+ str(BMI))
B=Button(w,text='CALCULATE',font =('arial',15),command =B_click)
B.place(x=150,y=220)
L3=Label(w,text ='BMI= ',font =('arial',15),fg ='green')
L3.place(x=180,y=280)

w.mainloop()
