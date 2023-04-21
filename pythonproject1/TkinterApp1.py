from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("200x150")
def fun():
    messagebox.showinfo("Hello, you have clicked red button")


def fun1():
    messagebox.showinfo("Hello, you have clicked blue button")

def fun2():
    messagebox.showinfo("Hello, you have clicked yellow button")

def fun3():
    messagebox.showinfo("Hello, you have clicked green button")


b1 = Button(top, text="Red", command = fun, activeforeground = "red", activebackground = "pink", pady = 10)
b2 = Button(top, text="Blue", command = fun1, activeforeground = "blue", activebackground = "pink", pady = 10)
b3 = Button(top, text="Green", command = fun2, activeforeground = "green", activebackground = "pink", pady = 10)
b4 = Button(top, text="Yellow", command = fun3, activeforeground = "yellow", activebackground = "pink", pady = 10)

b1.pack(side = LEFT)
b2.pack(side = RIGHT)
b3.pack(side = TOP)
b4.pack(side = BOTTOM)

top.mainloop()