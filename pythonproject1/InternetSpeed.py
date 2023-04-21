from tkinter import *
from tkinter import messagebox
import pyspeedtest
def logic():
    st = pyspeedtest.speedTest("www.google.com")
    a = (str(str.download()) +  ["Bytes per second."])
    messagebox.showinfo("Your download speed.")

top = Tk()
top.geometry("550x560+0+0")
top.title("My Speed Test")
b = Button(top, text="click to see the internet speed", font=('arial', 20), bg='yellow', height=1, width= 30, command=logic)\
    .pack()

top.mainloop()