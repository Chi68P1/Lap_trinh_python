from tkinter import *


A = Tk()
A.geometry("1000x700+400+50")
A.title("Text")

C =Canvas(master = A,bg ="white")
C.place(x=0,y=0,width = 700,height = 1000)

x1 = IntVar()
y1 = IntVar()
x2 = IntVar()
y2 = IntVar()
k = 0
a = 0
def B1_click():
	C.create_line(50,50,50,350,350,350,350,50,50,50,width = "1",fill ="red")

def B3_click():
	k = 1
	return k 

def B2_click():
	C.create_rectangle(200,200,500,500,outline = "green",fill = "green")

def B4_click():
	a=k+2
	return k

def nhan_chuot(event):
	x1.set(event.x)
	y1.set(event.y)

def nha_chuot(event):
	x2.set(event.x)
	y2.set(event.y)
	print(a)
	if k ==1:
		ve_hinh_3()
	else:
		ve_hinh_4()
	
def ve_hinh_4():

	C.create_oval(x1.get(),y1.get(),x2.get(),y2.get(),outline = "green",fill = "green")
def ve_hinh_3():

	C.create_rectangle(x1.get(),y1.get(),x2.get(),y2.get(),outline = "blue",fill = "blue")

def xoa(event):
	C.delete(ALL)

B1 = Button(master = A, text = "LINE", font = ("arial",15),bg = "green",fg = "white",command = B1_click)
B1.place(x=800,y=100)
B2 = Button(master = A, text = "ARC", font = ("arial",15),bg = "blue",fg = "white",command = B2_click)
B2.place(x=800,y=200)
B3 = Button(master = A, text = "RECT", font = ("arial",15),bg = "red",fg = "white",command = B3_click)
B3.place(x=800,y=300)
B4 = Button(master = A, text = "OVAL", font = ("arial",15),bg = "gray",fg = "white",command = B4_click)
B4.place(x=800,y=400)

C.bind("<Button-1>",nhan_chuot)
C.bind("<ButtonRelease-1>",nha_chuot)
C.bind("<Button-3>",xoa)


A.mainloop()