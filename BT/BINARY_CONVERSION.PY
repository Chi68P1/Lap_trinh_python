from tkinter import *
from tkinter import messagebox

W = Tk()
W.geometry("555x400+950+100")
W.title("BMI")


bin = lambda x : "".join(reversed( [str((x >> i) & 1) for i in range(8)] ) )

def B1_click():
	u = E1.get()
	if u =="":
		E2.delete(0,END)
		E2.insert(0,bin(int(0)))
	elif u.isdigit():
		E2.delete(0,END)
		E2.insert(0,bin(int(u)))
	else:
		messagebox.showinfo(title="Thông báo", message= "Nhập sai định dạng giá trị")
L1 = Label(master = W, text = "DECIMAL: ", font = ("arial",20))
L1.place(x=50,y=100,width=250,heigh=20)
L2 = Label(master = W, text = "BINARY: ", font = ("arial",20))
L2.place(x=42,y=170,width=250,heigh=20)

L3 = Label(master = W, text = "Nhập số tự nhiên không âm", font = ("arial",15)) 
L3.place(x=200,y=300)


E1 = Entry(master = W, font =("arial",15))
E1.place(x=250,y=95,width=150,heigh=30)
E2 = Entry(master = W, font =("arial",15))
E2.place(x=250,y=165,width=150,heigh=30)

B1 = Button(master = W, text ="CONVERT", font = ("arial",20),bg = "blue",fg = "white",command = B1_click)
B1.place(x=250,y=235,width=150,heigh=50)

#print("Số nhị phân tương ứng với {} là: ",bin(x).format(x))
W.mainloop()
