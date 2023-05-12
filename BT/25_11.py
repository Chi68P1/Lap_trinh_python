from tkinter import *
from tkinter import messagebox

W = Tk()
W.geometry("555x500+950+100")
W.title("BMI")

x = IntVar(value = 1)

def B1_click():
	x1= float(E1.get())
	x2= float(E2.get())
	if x.get() == 1:
		BMI= round(x2/(x1*x1),1)
	if x.get() == 2:
		BMI= round(x2*703/(x1*x1),1)

	#messagebox.showinfo("BMI",'BMI: '+str(BMI))
	w1 = Toplevel()
	w1.geometry("300x200+500+400")
	w1.title("BMI")
	w1.grab_set()

	def w1_destroy():
		w1.destroy()
	KQ = Label(master = w1, text = "", font = ("arial",20)) 
	KQ.place(x=30,y=50)
	KQ1 = Label(master = w1, text = "", font = ("arial",20)) 
	KQ1.place(x=30,y=120)
	B11 = Button(master = w1, text ='OK', font = ('arial',15),bg = "blue",fg = "white",command = w1_destroy)
	B11.place(x=160,y=80)


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



E1 = Entry(master = W, font =("arial",15),width = 10 )
E1.place(x=70,y=150,width=150,heigh=50)
E2 = Entry(master = W, font =("arial",15),width = 10 )
E2.place(x=70,y=300,width=150,heigh=50)

B1 = Button(master = W, text ='Caculate', font = ('arial',15),heigh= 3,width= 12,bg = "blue",fg = "white",command = B1_click)
B1.place(x=70,y=370,width=150,heigh=50)

def new():
	E1.delete(0,END)
	E2.delete(0,END)
	KQ.configure(text = "BMI")
	KQ1.configure(text = "")

def exit():
	M1 = messagebox.askyesno(title = "Thông báo",message = "Bạn có muốn thoát chương trình")
	if M1 == True:
		W.destroy()

def select_unit():
	if x.get() == 1:
		L2.configure(text = "Chiều cao: (m)")
		L3.configure(text = "Cân nặng: (kg)")
	if x.get() == 2:
		L2.configure(text = "Chiều cao: (Inches)")
		L3.configure(text = "Cân nặng: (Pounds)")
	

#thêm menu bar
Thanh_Menu = Menu(master = W)
W.configure(menu = Thanh_Menu)

#thêm Menu thành phần
file_menu = Menu(master = Thanh_Menu, tearoff = False)
Thanh_Menu.add_cascade(label = "File",menu = file_menu)

#thêm các tùy chọn điều khiển (item)
file_menu.add_command(label = "New",command = new)
file_menu.add_command(label = "Caculate",command  = B1_click)
file_menu.add_command(label = "Exit",command  = exit)

unit_menu = Menu(master = Thanh_Menu,tearoff = False)
Thanh_Menu.add_cascade(label = "Unit",menu = unit_menu)

unit_menu.add_radiobutton(label = "Metric",value = 1,variable = x,command = select_unit)
unit_menu.add_radiobutton(label = "English", value = 2,variable = x,command = select_unit)

W.mainloop()