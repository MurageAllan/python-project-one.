from tkinter import *
def addNumbers():
    res = int(e1.get()) + int(e2.get())
    addition.set(res)

def subtractNumbers():
    res1 = int(e1.get()) - int(e2.get())
    subtraction.set(res1)

def multiplyNumbers():
    res2 = int(e1.get()) * int(e2.get())
    multiplication.set(res2)

def divideNumbers():
    res3 = int(e1.get()) / int(e2.get())
    division.set(res3)

master = Tk()
master.geometry("300x300")
addition = StringVar()
subtraction = StringVar()
multiplication = StringVar()
division = StringVar()
Label(master, text="number one:").grid(row=0, sticky=W)
Label(master, text="number two:").grid(row=1, sticky=W)
Label(master, text="Add:").grid(row=3, sticky=W)
Label(master, text="subtract:").grid(row=4, sticky=W)
Label(master, text="Multiply:").grid(row=5, sticky=W)
Label(master, text="Divide:").grid(row=6, sticky=W)

result = Label(master,text=" ", textvariable=addition).grid(row=3, column=1, sticky=W)
result = Label(master,text=" ", textvariable=subtraction).grid(row=4, column=1, sticky=W)
result = Label(master,text=" ", textvariable=multiplication).grid(row=5, column=1, sticky=W)
result = Label(master,text=" ", textvariable=division).grid(row=6, column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b = Button(master, text="Sum", command=addNumbers).grid(row=6, column=1)
c = Button(master, text="Subtract", command=subtractNumbers).grid(row=7, column=1)
d = Button(master, text="Multiply", command=multiplyNumbers).grid(row=8, column=1)
e = Button(master, text="Divide", command=divideNumbers).grid(row=9, column=1)

master.mainloop()