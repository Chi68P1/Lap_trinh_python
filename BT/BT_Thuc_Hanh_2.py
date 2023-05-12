from tkinter import *
A = Tk()
A.geometry("450x500+900+100")
A.title("LENGTH CONVERSION")

E1 = Entry(master = A, font = ("arial",15))
E1.place(x = 200, y = 50,width = 120, height = 25)
E2 = Entry(master = A, font = ("arial",15))
E2.place(x = 200, y =190,width = 120, height = 25)
E3 = Entry(master = A, font = ("arial",15))
E3.place(x = 200, y = 260,width = 120, height = 25)

L1 = Label(master = A, text = "Feet:", font = ("arial",15))
L1.place(x=80,y=50)
L2 = Label(master = A, text = "Inches:", font = ("arial",15))
L2.place(x=80,y=190)
L3 = Label(master = A, text = "Centimeter:", font = ("arial",15))
L3.place(x=80,y=260)

L4 = Label(master = A, text = "", font = ("arial",15))
L4.place(x=200,y=380)

def B_click():
	m = 0
	n = 0
	if E1.get() == "":
		E2.delete(0,END)
		E2.insert(0,0)
		E3.delete(0,END)
		E3.insert(0,0)
		L4.configure(text = "")
	elif float(E1.get()) < 0:
		E2.delete(0,END)
		E3.delete(0,END)
		L4.configure(text = "Nhập lại giá trị ! ", fg = "red")
	else:
		m = float(E1.get())*12
		n = float(E1.get())*30.48
		E2.delete(0,END)
		E2.insert(0,round(m,1))
		E3.delete(0,END)
		E3.insert(0,round(n,1))
		L4.configure(text = "")

B = Button(master = A, text = "CONVERT", font = ("arial",15),bg = "blue", fg ="white",command = B_click)
B.place(x=200,y=330,width = 130, height = 30)

A.mainloop()