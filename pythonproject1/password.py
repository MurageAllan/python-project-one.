from tkinter import *

root = Tk()
root.geometry("900x500")

entry = Entry(root, show="*")
entry.pack(pady=100, ipadx=100, ipady=20 )

def show_password():
    if entry.cget("show") == "*":
        entry.config(show="")
    else:
        entry.config(show="*")



check_button = Checkbutton(root, text="show password", command=show_password)
check_button .place(x=290, y= 170)


root.mainloop()