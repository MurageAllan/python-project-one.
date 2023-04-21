from tkinter import *

root = Tk()
root.geometry("700x500+0+0")
root.configure(bg='powder blue')
root.title("Welcome to Python Programming Language Tkinter Menus")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)




root.config(menu=menubar)
root.mainloop()