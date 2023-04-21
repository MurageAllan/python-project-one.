from tkinter import *

root = Tk()

soda = StringVar()
water = StringVar()
juice = StringVar()
wine = StringVar()
coffee = StringVar()
milk = StringVar()
tea = StringVar()
matoke = StringVar()
rice = StringVar()
posho = StringVar()
meat = StringVar()
beans = StringVar()
vegetables = StringVar()
Total = StringVar()
Tax = StringVar()

text_input = StringVar()
operator = ""

htl = Label(root, text="HOTEL MANAGEMENT SYSTEM", font=('arial', 46, 'bold'))
htl.pack()

cont = Frame(root, relief=SUNKEN)
cont.pack(side=LEFT, fill=BOTH)

lbl1 = Label(cont, text="Customer Name", fg="blue")
lbl1.grid(row=0, column=0)
a = Entry(cont, relief=SUNKEN, width=60)
a.grid(row=0, column=1)

f8 = Frame(cont, relief=SUNKEN, height=300)
f8.place(x=10, y=30)

l = Label(f8, text="Cold Drinks", fg="blue")
l.grid(row=0, column=0)

l1 = Label(f8, text="Soda", fg="maroon", padx=6, pady=6)
l1.grid(row=1, column=0)
b = Entry(f8, width=30, bg="lightblue", textvariable=soda)
b.grid(row=1, column=1)
l2 = Label(f8, text="Water", fg="maroon", padx=6, pady=6)
l2.grid(row=2, column=0)
c = Entry(f8, width=30, bg="lightblue", textvariable=water)
c.grid(row=2, column=1)
l3 = Label(f8, text="Juice", fg="maroon", padx=6, pady=6)
l3.grid(row=3, column=0)
d = Entry(f8, width=30, bg="lightblue", textvariable=juice)
d.grid(row=3, column=1)
l4 = Label(f8, text="Wine", fg="maroon", padx=6, pady=6)
l4.grid(row=4, column=0)
e = Entry(f8, width=30, bg="lightblue", textvariable=wine)
e.grid(row=4, column=1)

f3 = Frame(cont, relief=SUNKEN)
f3.place(x=30, y=260)

l5 = Label(f3, text="Hot Drinks", fg="blue")
l5.grid(row=0, column=0)
l6 = Label(f3, text="Coffee", fg="maroon", padx=6, pady=6)
l6.grid(row=1, column=0)
f = Entry(f3, width=27, bg="lightblue", textvariable=coffee)
f.grid(row=1, column=1)
l7 = Label(f3, text="Milk", fg="maroon", padx=6, pady=6)
l7.grid(row=2, column=0)
j = Entry(f3, width=27, bg="lightblue", textvariable=milk)
j.grid(row=2, column=1)
l8 = Label(f3, text="Black Tea", fg="maroon", padx=6, pady=6)
l8.grid(row=3, column=0)
k = Entry(f3, width=27, bg="lightblue", textvariable=tea)
k.grid(row=3, column=1)

f4 = Frame(cont, relief=SUNKEN)
f4.place(x=270, y=30)

lb1 = Label(f4, text="Foods", fg='blue', padx=6, pady=6)
lb1.grid(row=0, column=0)

lb2 = Label(f4, text="Matoke", fg="maroon", padx=6, pady=6)
lb2.grid(row=1, column=0)
l = Entry(f4, width=30, bg="lightblue", textvariable=matoke)
l.grid(row=1, column=1)
lb3 = Label(f4, text="Rice", fg="maroon", padx=6, pady=6)
lb3.grid(row=2, column=0)
m = Entry(f4, width=30, bg="lightblue", textvariable=rice)
m.grid(row=2, column=1)
lb4 = Label(f4, text="Posho", fg="maroon", padx=6, pady=6)
lb4.grid(row=3, column=0)
n = Entry(f4, width=30, bg="lightblue", textvariable=posho)
n.grid(row=3, column=1)

f5 = Frame(cont, relief=SUNKEN)
f5.place(x=270, y=260)

lbl2 = Label(f5, text="Sauce", fg="blue", padx=6, pady=6)
lbl2.grid(row=0, column=0)

lbl3 = Label(f5, text="Meat", fg="maroon", padx=6, pady=6)
lbl3.grid(row=1, column=0)
o = Entry(f5, width=30, bg="lightblue", textvariable=meat)
o.grid(row=1, column=1)
lbl4 = Label(f5, text="Beans", fg="maroon", padx=6, pady=6)
lbl4.grid(row=2, column=0)
p = Entry(f5, width=30, bg="lightblue", textvariable=beans)
p.grid(row=2, column=1)
lbl5 = Label(f5, text="Vegetables", fg="maroon", padx=6, pady=6)
lbl5.grid(row=3, column=0)
q = Entry(f5, width=30, bg="lightblue", textvariable=vegetables)
q.grid(row=3, column=1)


cont1 = Frame(root, relief=SUNKEN)
cont1.pack(side=LEFT, fill=BOTH)

f6 = Frame(cont1, relief=SUNKEN)
f6.grid(row=0, column=0)

x = Label(f6, text="Reciept", fg='blue')
x.grid(row=0, column=0)
r = Frame(f6, width=350, bg='white', height=300)
r.grid(row=1, column=0)

f7 = Frame(cont1, relief=SUNKEN)
f7.grid(row=1)

def Totals():
    try:c1 = int(soda.get())
    except:c1 = 0
    try:c2 = int(water.get())
    except:c2 = 0
    try:c3 = int(juice.get())
    except:c3 = 0
    try:c4 = int(wine.get())
    except:c4 = 0
    try:c5 = int(coffee.get())
    except:c5 = 0
    try:c6 = int(milk.get())
    except:c6 = 0
    try:c7 = int(tea.get())
    except:c7 = 0
    try:c8 = int(matoke.get())
    except:c8 = 0
    try:c9 = int(rice.get())
    except:c9 = 0
    try:c10 = int(posho.get())
    except:c10 = 0
    try:c11 = int(meat.get())
    except:c11 = 0
    try:c12 = int(beans.get())
    except:c12 = 0
    try:c13 = int(vegetables.get())
    except:c13 = 0

    d1=c1*100
    d2=c2*30
    d3=c3*100
    d4=c4*400
    d5=c5*70
    d6=c6*100
    d7=c7*80
    d8=c8*70
    d9=c9*90
    d10=c10*100
    d11=c11*50
    d12=c12*50
    d13=c13*50

    totalcost = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12+d13
    ax = (totalcost*7)/100
    string_tax = "Ksh.", str('%.f7' % ax)
    Tax.set(string_tax)
    string_bill = "Ksh.", str('%.f7' % totalcost)
    Total.set(string_bill)


tax = Label(f7, text="Tax", pady=8, padx=8, fg="maroon")
tax.grid(row=0, column=0)
tax_entry = Entry(f7, width=40, bg='powderblue', bd=3, textvariable=Tax)
tax_entry.grid(row=0, column=1)
total = Button(f7, text="Totals", pady=8, padx=8, fg="maroon", command=Totals)
total.grid(row=1, column=0)
total_entry = Entry(f7, width=40, bg='powderblue', bd=3, textvariable=Total)
total_entry.grid(row=1, column=1)

def Reset():
    b.delete(0, END)
    c.delete(0, END)
    d.delete(0, END)
    e.delete(0, END)
    f.delete(0, END)
    j.delete(0, END)
    k.delete(0, END)
    l.delete(0, END)
    m.delete(0, END)
    n.delete(0, END)
    o.delete(0, END)
    p.delete(0, END)
    q.delete(0, END)

def Exit():
    root.destroy()

b1 = Button(f7, text="Print Reciept", pady=8, padx=8, fg="maroon")
b1.grid(row=2, column=0)
b2 = Button(f7, text="Reset", pady=8, padx=8, fg="maroon", command=Reset)
b2.grid(row=2, column=1)
b3 = Button(f7, text="Exit", pady=8, padx=8, fg="maroon", command=Exit)
b3.grid(row=2, column=2)

f8 = Frame(cont1, height=50)
f8.grid(row=0, column=1)
l8 = Label(f8, text="calculator")
l8.grid(row=0, column=0)

def btnclicked(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")


def btnequals():
    global operator
    sumup = str(eval(operator))
    operator = " "
    text_input.set(sumup)

td = Entry(f8, font=x, textvariable=text_input, bd=5, insertwidth=4, bg='yellow', justify='right').grid(columnspan=4)

btn7 = Button(f8, padx=8, pady=8, fg='black', bd=8, font=x, text=7, command=lambda:btnclicked(7)).grid(row=2, column=0)
btn8 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='8', command=lambda:btnclicked(8)).grid(row=2, column=1)
btn9 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='9', command=lambda:btnclicked(9)).grid(row=2, column=2)
btna = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='+', command=lambda:btnclicked('+')).grid(row=2, column=3)
btn4 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='4', command=lambda:btnclicked(4)).grid(row=3, column=0)
btn5 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='5', command=lambda:btnclicked(5)).grid(row=3, column=1)
btn6 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='6', command=lambda:btnclicked(6)).grid(row=3, column=2)
btns = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='-', command=lambda:btnclicked('-')).grid(row=3, column=3)
btn1 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='1', command=lambda:btnclicked(1)).grid(row=4, column=0)
btn2 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='2', command=lambda:btnclicked(2)).grid(row=4, column=1)
btn3 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='3', command=lambda:btnclicked(3)).grid(row=4, column=2)
btnm = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='', command=lambda:btnclicked('')).grid(row=4, column=3)
btn0 = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='0', command=lambda:btnclicked(0)).grid(row=5, column=0)
btn_d = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='.', command=lambda:btnclicked('.')).grid(row=5, column=1)
btnc = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='c', command=btncleardisplay).grid(row=5, column=2)
btne = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='=', command=btnequals, width=15).grid(columnspan=6)
btnd = Button(f8, padx=8, pady=8, bd=5, fg='black', font=x, text='/', command=lambda:btnclicked('/')).grid(row=5, column=3)

root.mainloop()