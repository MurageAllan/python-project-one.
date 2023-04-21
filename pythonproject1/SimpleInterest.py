from tkinter import *
root=Tk()

root.geometry("500x300")
root.title("Simple Interest")
def calculate():
    prin=int(principleentry.get())
    rat=int(rateentry.get())
    tin=int(timeentry.get())
    amount=(prin*rat*tin)/100
    Label(text=f"{amount}" , font="arial 30 bold" ,fg="white" , bg="black").place(x=200 , y=220)

def exit():
    root.destroy()

principle=Label(root,text="Principle" , font="arial 15")
rate=Label(root,text="Rate of Interest:" , font="arial 15")
time=Label(root, text="Time" , font="arial 15")

principle.place(x=50 , y=20)
rate.place(x=50 , y=90)
time.place(x=50 , y=160)

interest=Label(root , text="Interest" , font="arial 15",fg="blue")
interest.place(x=50 , y=230)


principlevalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()

principleentry=Entry(root , textvariable=principlevalue, font="arial 20" , width=8)
rateentry=Entry(root , textvariable=ratevalue, font="arial 20" , width=8)
timeentry=Entry(root , textvariable=timevalue, font="arial 20" , width=8)

principleentry.place(x=220 , y=20)
rateentry.place(x=220 , y=90)
timeentry.place(x=220 ,y=160)

Button(text="Calculate" , font="arial 15" , command=calculate).place(x=350 , y=20)
Button(root, text="Exit" , font="arial 15" , width=8, command=exit).place(x=350 , y=90)

root.mainloop()
