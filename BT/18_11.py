from tkinter import *
from tkinter import filedialog
A = Tk()
A.geometry("1000x700+400+50")
A.title("Text")

T =Text(master = A, font = ("arial",15))
T.pack(expand = True, fill = "both")

s = IntVar(value =13)

def B1_click():
	D1 = filedialog.askopenfile(mode= "r")
	f = open(file = D1.name,mode = "r",encoding = "utf-8")
	A = f.read()
	T.delete("1.0",END)
	T.insert("1.0",A)
	f.close()

def B2_click():
	D2 = filedialog.asksaveasfile(mode = "w")
	f = open(file = D2.name,mode = "w",encoding = "utf-8")
	f.write(T.get("1.0",END))
	f.close()

def fontsize_change():
	T.configure(font = ("arial",s.get()))


menu_bar = Menu(master = A)
A.configure(menu = menu_bar)

file_menu = Menu(master = menu_bar,tearoff = False)
view_menu = Menu(master = menu_bar,tearoff = False)
help_menu = Menu(master = menu_bar,tearoff = False)
menu_bar.add_cascade(label = "File",menu = file_menu)
menu_bar.add_cascade(label = "View",menu = view_menu)
menu_bar.add_cascade(label = "Help",menu = help_menu)

file_menu.add_command(label = "Open",command = B1_click)
file_menu.add_command(label = "Save",command = B2_click)

view_menu.add_radiobutton(label = "50%",value  = 8,variable = s,command = fontsize_change)
view_menu.add_radiobutton(label = "100%",value  = 13,variable = s,command = fontsize_change)
view_menu.add_radiobutton(label = "200%",value  = 20,variable = s,command = fontsize_change)

A.mainloop()