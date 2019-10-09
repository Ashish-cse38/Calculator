from tkinter import *

window=Tk()

window.wm_title("Calculator")

def calcAdd():
  result=(float(num1_value.get())+float(num2_value.get()))
  t1.delete(1.0,END)
  t1.insert(END,result)

def calc_sub():
  result=(float(num1_value.get())-float(num2_value.get()))
  t1.delete(1.0,END)
  t1.insert(END,result)

def calc_div():
  result=(float(num1_value.get())/float(num2_value.get()))
  t1.delete(1.0,END)
  t1.insert(END,result)

def calc_mul():
  result=(float(num1_value.get())*float(num2_value.get()))
  t1.delete(1.0,END)
  t1.insert(END,result)


l1=Label(window,text="num1")
l1.grid(row=0,column=0)

l2=Label(window,text="num2")
l2.grid(row=0,column=1)


num1_value=StringVar()
num1=Entry(window,textvariable=num1_value)
num1.grid(row=1,column=0)

num2_value=StringVar()
num2=Entry(window,textvariable=num2_value)
num2.grid(row=1,column=1)


b1=Button(window,text="
          ",command=calcAdd)
b1.grid(row=2,column=0)

b1=Button(window,text="SUBTRACT",command=calc_sub)
b1.grid(row=2,column=1)

b1=Button(window,text="MULTIPLY",command=calc_mul)
b1.grid(row=3,column=0)

b1=Button(window,text="DIVIDE",command=calc_div)
b1.grid(row=3,column=1)


t1=Text(window,height=1,width=20)
t1.grid(row=4,column=0)

window.mainloop()
