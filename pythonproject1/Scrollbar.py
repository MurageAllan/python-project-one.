from tkinter import *
def add():
    addition = "value = " + str(v.get())
    Label.config(text = addition)

top = Tk()
top.geometry("200x100")
v = DoubleVar()
scale = Scale(top, variable = v, from_=1, to = 50, orient = HORIZONTAL)
scale.pack(anchor=CENTER)

btn = Button(top, text="Value", command=add)
btn.pack(anchor=CENTER)

Label = Label(top)
Label.pack()

top.mainloop()