from tkinter import  *

def allow():
    ans = int(eb.get()) * 0.15
    allowances.set(ans)
    ans1 = int(eb.get()) * 0.30
    deductions.set(ans1)
    ans2 = int(eb.get()) + ans
    grosspays.set(ans2)
    ans3 = ans2 + ans1
    netpays.set(ans3)


root = Tk()
allowances = StringVar()
deductions = StringVar()
grosspays = StringVar()
netpays = StringVar()

root.title("Program Calculator")
root.geometry("1700x1000")
root.config(bg= "gray")

basic_p = Label(root, text="Basic Pay").place(x=50, y=20)
allowance = Label(root, text="Allowance").place(x=50, y= 80)
deduction = Label(root, text="Deductions").place(x=50, y= 140)
gross_pay = Label(root, text="Gross pay").place(x=50, y= 200)
net_pay = Label(root, text="Net pay").place(x=50, y= 260)

eb= Entry(root, font="arial")
eb.place(x = 200, y=20)
eb= Entry(root, font="arial", textvariable=allowances)
eb.place(x = 200, y=80)
eb= Entry(root, font="arial", textvariable=deductions)
eb.place(x = 200, y=140)
eb= Entry(root, font="arial", textvariable=grosspays)
eb.place(x = 200, y=200)
eb= Entry(root, font="arial", textvariable=netpays)
eb.place(x = 200, y=260)

calculate = Button(root, text="calculate", fg="black", bg="#06588E", command=allow).place(x=250, y=350)

root.mainloop()
