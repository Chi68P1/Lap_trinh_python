'''print('Brian\"s mother: He\'s not an angel. He\'s a very naughty boy!')
print("""this
is a
multiline
text""") 
num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")
while False:
  print("Looping...")'''
#your code goes here
'''print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(","))
#prints "['spam', 'eggs', 'ham']"
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)'''
'''import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
print(heights_arr)
print((heights_arr > 188).sum())'''
from tkinter import *

W=Tk()
W.geometry('800x600+600+200')
W.title('Soạn thảo văn bản')

C1=Canvas(master=W,bg='white')
C1.place(x=0,y=0,width=600,height=600)

v=IntVar()
def B1_click():
    v.set(0)
def B2_click():
    v.set(1)
def B3_click():
    v.set(2)
def B4_click():
    v.set(3)
def B5_click():
    C1.delete(ALL)



B1=Button(W,text='LINE',font=('arial',15),width=10,bg='green',fg='white',command=B1_click)
B1.place(x=630,y=100)
B2=Button(W,text='ARC',font=('arial',15),width=10,bg='blue',fg='white',command=B2_click)
B2.place(x=630,y=150)
B3=Button(W,text='RECT',font=('arial',15),width=10,bg='red',fg='white',command=B3_click)
B3.place(x=630,y=200)
B4=Button(W,text='OVAL',font=('arial',15),width=10,bg='orange',fg='white',command=B4_click)
B4.place(x=630,y=250)
B5=Button(W,text='DELETE',font=('arial',15),width=10,bg='gray',fg='white',command=B5_click)
B5.place(x=630,y=300)

def ve_hinh(event):
    x=event.x
    y=event.y
    if v.get()==0:
        C1.create_line(x,y,x+100,y+100,width=10,tags='H1')
    elif v.get()==1:
        C1.create_arc(x,y,x+200,y+400,start=0,extent=120,width=5,outline='green',fill='blue',style=PIESLICE)
    elif v.get()==2:
        C1.create_rectangle(x,y,x+20,y+10,width=3,outline='green',fill='green',tags='H2')
    else:
        C1.create_oval(x,y,x+100,y+200,width=3,outline='#9D4FEE',fill='#9D4FEE')
def xoa_hinh(event):
    C1.delete(ALL)
C1.bind('<Button-1>',ve_hinh)
C1.bind('<Button-3>',xoa_hinh)

W.mainloop()