from Tkinter import *
top = Tk()
top.geometry("400x250")
name = Label(top, text = "Name").place(x = 30, y = 50)
email = Label(top, text = "email").place(x = 30, y = 90)
password = Label(top, text = "password").place(x = 30, y = 130)
cost = Label(top, text = "cost").place(x = 30, y = 170)
department = Label(top, text = "department").place(x = 30, y = 210)
cost = Label(top, text = "cost").place(x = 30, y = 250)



top.mainloop()