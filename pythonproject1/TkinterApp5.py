from tkinter import *
def areaCircle():
    res = int(e1.get()) ** 2 * 3.142
    area.set(res)

master = Tk()
area = StringVar()
master.geometry("300x300")
Label(master, text="radius:").grid(row=0, sticky=W)
Label(master, text="Area:").grid(row=3, sticky=W)
result = Label(master,text=" ", textvariable=area).grid(row=3, column=1, sticky=W)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Area", command=areaCircle).grid(row=6, column=1)

master.mainloop()