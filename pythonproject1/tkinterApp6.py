from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry('500x300')

L1 = Label(window, text='Post your comments')
L1.pack()
textbox = Text(window, width=20, height=10)
textbox.pack()

L2 = Label(window, text='Select your State')
L2.pack()
item = StringVar()

combobox = Combobox(window, textvariable=item,values=['Nairobi', 'Nakuru', 'Mombasa', 'Kisumu', 'Eldoret'])
combobox.pack()

L3 = Label(window, text='Select your Skill sets')
L3.pack()

listbox = Listbox(window, selectmode=MULTIPLE)
listbox.insert(1, 'C')
listbox.insert(2, 'C++')
listbox.insert(3, 'Java')
listbox.insert(4, 'Javascript')
listbox.insert(5, 'Python')
listbox.pack()

def myFunction():
    # data = textbox.get(1, 0, END)
    # data = item.get()
    data = ' '
    for i in listbox.curselection():
        data += listbox.get(i)
    emptylabel.config(text=data)

Button(window, text='click', command=myFunction).pack()

emptylabel = Label(window)
emptylabel.pack()


window.mainloop()