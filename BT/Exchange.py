from tkinter import *

W = Tk()
W.geometry('500x400+400+200')

F1 = Frame(master=W)
F1.place(x = 50,y = 30)
F2 = Frame(master=W)
F2.place(x = 270, y = 30)

L1 = Label(master=W,text = 'GIÁ TRỊ QUY ĐỔI: ',font = ('arial',15),fg = 'blue')
L1.place(x = 120, y = 250)

L = ['USD: 22.000đ','EUR: 26.000đ','JPY: 200đ']
PT = StringVar(value = L)

LB1 = Listbox(master=F1,font = ('arial',15),width = 12,height = 6,listvariable=PT)
LB1.pack()

def B1_click():
    m = 0
    A = 0
    if E1.get() != '':
        m = float(E1.get())
    x = LB1.curselection()
    if x[0] == 0:
        A = m*22000
    elif x[0] == 1:
        A = m*26000
    elif x[0] == 2:
        A = m*200
    L1.configure(text='GÍA TRỊ QUY ĐỔI: {:,} VND'.format(A))


E1 = Entry(master=F2,font = ('arial',15),width = 12)
E1.grid(row = 0,column=0,pady = 30,sticky='w')
B1 = Button(master=F2,text = 'EXCHANGE',font = ('arial',15),width = 12,bg = 'blue',fg = 'white',command=B1_click)
B1.grid(row = 1,column=0,pady = 0,sticky='w')

W.mainloop()