from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
import tempfile
import time
root=Tk()
root.geometry("1300x620+20+20")
root.title("Nyamu Murage")
toplbl=Label(root,text="HOTEL MANAGEMENT",font=('arial',36,'bold'))
toplbl.place(x=200,y=0)
mycanvas=Canvas(root,width=1300,height=5)
line=mycanvas.create_line(0,0,1300,0,width=10,fill="powder blue")
mycanvas.place(x=0,y=50)
name=Label(root,text="Customer Name",font=('arial',16,'bold'),fg="navy")
name.place(x=0,y=65)
lblentry=Entry(root,font=('arial',15))
lblentry.place(x=180,y=60,width=430,height=30)
mycanvas2=Canvas(root,width=620,height=15)
line2=mycanvas2.create_line(0,0,620,0,width=15,fill="blue")
mycanvas2.place(x=0,y=95)

#loading
def loading():
    for i in range(1,101,1):
        pb["value"]=i
        load.update_idletasks()
        pl.config(text=str(i)+"%")
        time.sleep(0.01)
    pb["value"]=100
    top.deiconify()
    load.destroy()
load=Toplevel()
load.geometry("400x200+400+100")
load.title("loading...")
load.configure(bg="pink")
pl=Label(load,font=("consolas 18 bold"),fg="cyan",bg="pink")
pl.place(x=170,y=60)
pb=Progressbar(load,orient='horizontal',mode='determinate',length=300,)
pb.place(x=20,y=120)
label=Label(load,text="Login Form is Loading...",fg='white',font=("forte 18"),bg="pink")
label.pack(side=TOP)
label2=Label(load,text="Kindly Wait....",fg='white',bg="pink")
label2.place(x=150,y=90)
start=Button(load,text='Start',command=loading)
start.place(x=40,y=160)
#login
def login():
    if entry1.get() == '' and entry2.get() == '':
        success.set("Enter your login credentials")
    else:
        if entry1.get() == 'Allan' and entry2.get() == '3087':
            root.deiconify()
            top.destroy()
        else:
            success.set("You entered wrong username or paasword.")
global success
success=StringVar()

def exit1():
    root.destroy()
    top.destroy()
    sys.exit()
top=Toplevel()
top.geometry('400x300+300+100')
top.title("Nyamu Allan")
top.configure(bg='powder blue')

# lbl7=Label(top,text='USER LOGIN',font=('lucida calligraphy',20,'bold'),fg='gold', bg='powder blue',bd=15)
lbl0=Label(top,text='Hotel Management System',font=('lucida calligraphy',15),fg='gold',
           bg='powder blue',bd=15)
lbl1=Label(top,text='Username',font=('gabriola',15,'bold'),fg='gold',bg='powder blue',bd=15)
lbl2=Label(top,text='Password',font=('gabriola',15,'bold'),fg='gold',bg='powder blue',bd=15)
entry1=Entry(top)
entry2=Entry(top,show="*")
lbl=Label(top,text="",textvariable=success,font=('arial',12),bg='powder blue',fg="white")
btn2=Button(top,text='Cancel',fg='white',bg='black',font=('arial',15,'bold'),command=exit1)
btn1=Button(top,text="Login",fg='white',bg='black',font=('arial',15,'bold'),command=login)
lbl8=Label(top,text='By: Nyamu Murage ',font=('Helvetica',8),bg='powder blue')
lbl0.place(x=90,y=0)
# lbl7.place(x=110,y=40)
lbl1.place(x=130,y=80)
entry1.place(x=130,y=120)
lbl2.place(x=130,y=140)
entry2.place(x=130,y=180)
lbl.place(x=130,y=200)
btn2.place(x=20,y=240)
btn1.place(x=300,y=240)
lbl8.place(x=130,y=280)
#cold drinks
f1=Frame(root,width=300,height=485)
f1.place(x=0,y=105)
canvas1=Canvas(f1,width=295,height=480)
rectangle=canvas1.create_rectangle(3,15,290,475,outline="dim grey")
canvas1.place(x=3,y=5)
colddrinks=Label(f1,text="Cold Drinks",font=('arial',18,'bold'),fg="blue")
colddrinks.place(x=15,y=5)
soda=Label(f1,text="Soda",font=('arial',16,'bold'),fg="firebrick")
soda.place(x=15,y=55)
sodaentry=Entry(f1,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
sodaentry.place(x=110,y=55,width=180,height=30)
water=Label(f1,text="Water",font=('arial',16,'bold'),fg="firebrick")
water.place(x=15,y=105)
waterentry=Entry(f1,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
waterentry.place(x=110,y=105,width=180,height=30)
juice=Label(f1,text="Juice",font=('arial',16,'bold'),fg="firebrick")
juice.place(x=15,y=155)
juiceentry=Entry(f1,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
juiceentry.place(x=110,y=155,width=180,height=30)
wine=Label(f1,text="Wine",font=('arial',16,'bold'),fg="firebrick")
wine.place(x=15,y=205)
wineentry=Entry(f1,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
wineentry.place(x=110,y=205,width=180,height=30)

#foods
f2=Frame(root,width=310,height=490)
f2.place(x=301,y=105)
canvas2=Canvas(f2,width=305,height=485)
rectangle2=canvas2.create_rectangle(3,15,300,480,outline="dim grey")
canvas2.place(x=3,y=5)
foods=Label(f2,text="Foods",font=('arial',18,'bold'),fg="blue")
foods.place(x=15,y=5)
matoke=Label(f2,text="Matoke",font=('arial',16,'bold'),fg="firebrick")
matoke.place(x=15,y=65)
matokeentry=Entry(f2,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
matokeentry.place(x=110,y=65,width=190,height=30)
rice=Label(f2,text="Rice",font=('arial',16,'bold'),fg="firebrick")
rice.place(x=15,y=125)
riceentry=Entry(f2,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
riceentry.place(x=110,y=125,width=190,height=30)
posho=Label(f2,text="Posho",font=('arial',16,'bold'),fg="firebrick")
posho.place(x=15,y=185)
poshoentry=Entry(f2,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
poshoentry.place(x=110,y=185,width=190,height=30)

#hot drinks
f3=Frame(f1,width=280,height=235)
f3.place(x=10,y=241)
canvas3=Canvas(f3,width=275,height=230)
rectangle3=canvas3.create_rectangle(5,15,270,225,outline="dim grey")
canvas3.place(x=5,y=5)
hotdrinks=Label(f3,text="Hot Drinks",font=('arial',18,'bold'),fg="blue")
hotdrinks.place(x=15,y=5)
coffee=Label(f3,text="Coffee",font=('arial',16,'bold'),fg="firebrick")
coffee.place(x=15,y=45)
coffeeentry=Entry(f3,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
coffeeentry.place(x=120,y=45,width=150,height=30)
milk=Label(f3,text="Milk",font=('arial',16,'bold'),fg="firebrick")
milk.place(x=15,y=105)
milkentry=Entry(f3,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
milkentry.place(x=120,y=105,width=150,height=30)
blacktea=Label(f3,text="Black Tea",font=('arial',16,'bold'),fg="firebrick")
blacktea.place(x=15,y=165)
blackteaentry=Entry(f3,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
blackteaentry.place(x=120,y=165,width=150,height=30)

#sauce
f4=Frame(f2,width=290,height=270)
f4.place(x=10,y=211)
canvas4=Canvas(f4,width=285,height=265)
rectangle4=canvas4.create_rectangle(5,15,280,255,outline="dim grey")
canvas4.place(x=5,y=5)
sauce=Label(f4,text="Sauce",font=('arial',18,'bold'),fg="blue")
sauce.place(x=15,y=5)
meat=Label(f4,text="Meat",font=('arial',16,'bold'),fg="firebrick")
meat.place(x=15,y=65)
meatentry=Entry(f4,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
meatentry.place(x=130,y=65,width=150,height=30)
beans=Label(f4,text="Beans",font=('arial',16,'bold'),fg="firebrick")
beans.place(x=15,y=125)
beansentry=Entry(f4,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
beansentry.place(x=130,y=125,width=150,height=30)
vegies=Label(f4,text="Vegetables",font=('arial',16,'bold'),fg="firebrick")
vegies.place(x=15,y=185)
vegiesentry=Entry(f4,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT)
vegiesentry.place(x=130,y=185,width=150,height=30)

#receipt
f5=Frame(root,width=375,height=430)
f5.place(x=606,y=55)
canvas5=Canvas(f5,width=370,height=425)
rectangle5=canvas5.create_rectangle(5,15,365,420,outline="dim grey")
canvas5.place(x=5,y=5)
receipt=Label(f5,text="Receipt",font=('arial',18,'bold'),fg="blue")
receipt.place(x=15,y=5)
txt=Text(f5,width=42,height=22,wrap=WORD)
txt.place(x=20,y=50)

#calculator
f6=Frame(root,width=315,height=430)
f6.place(x=981,y=55)
canvas6=Canvas(f6,width=310,height=425)
rectangle6=canvas6.create_rectangle(5,5,300,420,outline="dim grey")
canvas6.place(x=5,y=5)
calc=Label(f6,text="Calculator",font=('arial',12),fg="black")
calc.place(x=15,y=0)

text_input=StringVar()
operator=""

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator=""
    text_input.set("")

def btnequals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
txtDisplay=Entry(f6,font=('arial',20,'bold'),textvariable=text_input,bd=8,insertwidth=4,
                 bg='yellow',justify='right')
txtDisplay.place(x=15,y=20,width=280)

b7=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='7',
          command=lambda:btnclick(7)).place(x=15,y=70)
b8=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='8',
          command=lambda:btnclick(8)).place(x=85,y=70)
b9=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='9',
          command=lambda:btnclick(9)).place(x=155,y=70)
baddition=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='+',width=2,
                 command=lambda:btnclick("+")).place(x=225,y=70)

b4=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='4',
          command=lambda:btnclick(4)).place(x=15,y=140)
b5=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='5',
          command=lambda:btnclick(5)).place(x=85,y=140)
b6=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='6',
          command=lambda:btnclick(6)).place(x=155,y=140)
bsubtraction=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='-',width=2,
                 command=lambda:btnclick("-")).place(x=225,y=140)

b1=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='1',
          command=lambda:btnclick(1)).place(x=15,y=210)
b2=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='2',
          command=lambda:btnclick(2)).place(x=85,y=210)
b3=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='3',
          command=lambda:btnclick(3)).place(x=155,y=210)
bmultiplication=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='*',width=2,
                 command=lambda:btnclick("*")).place(x=225,y=210)

b0=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='0',
          command=lambda:btnclick(0)).place(x=15,y=280)
bdecimal=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='.',
          command=lambda:btnclick(".")).place(x=85,y=280)
bclear=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='C',
          command=lambda:btncleardisplay()).place(x=155,y=280)
bdivision=Button(f6,padx=12,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='/',width=2,
                 command=lambda:btnclick("/")).place(x=225,y=280)

bequals=Button(f6,padx=16,pady=6,bd=4,fg="black",font=('arial',20,'bold'),text='=',width=14,
               command=btnequals).place(x=15,y=350)

def Reset():
    lblentry.delete(0,END)
    sodaentry.delete(0,END)
    waterentry.delete(0,END)
    juiceentry.delete(0, END)
    wineentry.delete(0, END)
    coffeeentry.delete(0, END)
    milkentry.delete(0, END)
    blackteaentry.delete(0, END)
    matokeentry.delete(0, END)
    riceentry.delete(0, END)
    poshoentry.delete(0, END)
    meatentry.delete(0, END)
    beansentry.delete(0, END)
    vegiesentry.delete(0, END)
    taxentry.delete(0, END)
    totalentry.delete(0, END)
    txt.delete('0.0',END)

def Exit():
    Exit=messagebox.askyesno("Quit System","Do you want to Quit?")
    if Exit>0:
        root.destroy()
        return
def printreceipt():
    r= txt.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(r)
    os.startfile(filename, "print")


# total
def Total():
    try:
        a1=int(sodaentry.get())
    except:
        a1=0
    try:
        a2=int(waterentry.get())
    except:
        a2=0
    try:
        a3=int(juiceentry.get())
    except:
        a3=0
    try:
        a4=int(wineentry.get())
    except:
        a4=0
    try:
        a5 =int(coffeeentry.get())
    except:
        a5 = 0
    try:
        a6 =int(milkentry.get())
    except:
        a6 = 0
    try:
        a7 =int(blackteaentry.get())
    except:
        a7 = 0
    try:
        a8=int(matokeentry.get())
    except:
        a8=0
    try:
        a9=int(riceentry.get())
    except:
        a9=0
    try:
        a10=int(poshoentry.get())
    except:
        a10=0
    try:
        a11 =int(meatentry.get())
    except:
        a11 = 0
    try:
        a12=int(beansentry.get())
    except:
        a12=0
    try:
        a13=int(vegiesentry.get())
    except:
        a13=0

    sodaprice = 40.0
    waterprice = 30.0
    juiceprice = 50.0
    wineprice = 200.0
    matokeprice = 80.0
    riceprice = 40.0
    poshoprice = 70.0
    coffeeprice = 30.0
    milkprice = 40.0
    blackteaprice = 25.0
    meatprice = 100.0
    beansprice = 35.0
    vegiesprice = 30.0

    totsoda = float(a1) * sodaprice
    totwater = float(a2) * waterprice
    totjuice = float(a3) * juiceprice
    totwine = float(a4) * wineprice
    totcoffee = float(a5) * coffeeprice
    totmilk = float(a6) * milkprice
    totblacktea = float(a7) * blackteaprice
    totmatoke = float(a8) * matokeprice
    totrice = float(a9) * riceprice
    totposho = float(a10) * poshoprice
    totmeat = float(a11) * meatprice
    totbeans = float(a12) * beansprice
    totvegies = float(a13) * vegiesprice

    totalcost = (totsoda + totwater + totjuice + totwine + totcoffee + totmilk + totblacktea + totmatoke
                 + totrice + totposho + totmeat + totbeans + totvegies)
    paytax = (totalcost * 0.06)
    tax.set(paytax)
    overall="Kshs",(paytax + totalcost)
    mytotal.set(overall)

    sentense = ("    THE IYANI'S\' HOTEL\n" + "Hello, " + lblentry.get() + "\n Items   Amount   price"
                                                                           "\n  Soda       " + str(
        sodaentry.get()) + "      " +
                str(sodaprice) + "\n  Water      " + str(waterentry.get()) + "      " +
                str(waterprice) + "\n  Juice      " + str(juiceentry.get()) + "      " +
                str(juiceprice) + "\n  Wine       " +
                str(wineentry.get()) + "      " + str(wineprice) + "\n  Matoke     " +
                str(matokeentry.get()) + "      " + str(matokeprice)
                + "\n  Rice       " + str(riceentry.get()) + "      " + str(riceprice) + "\n  Posho      " +
                str(poshoentry.get()) + "      " + str(poshoprice) + "\n  Coffee     "
                + str(coffeeentry.get()) + "      " + str(coffeeprice) + "\n  Milk       " +
                str(milkentry.get()) + "      " + str(milkprice) + "\n  Black Tea  " +
                str(blackteaentry.get()) + "      " + str(blackteaprice) + "\n  Meat       " +
                str(meatentry.get()) + "      " + str(meatprice) + "\n  Beans      " +
                str(beansentry.get()) + "      " +
                str(beansprice) + "\n  Vegetables " + str(vegiesentry.get()) + "      " +
                str(vegiesprice) + "\n\n  Tax   " + str(taxentry.get()) + "\n\n  Total   " +
                str(totalentry.get()) +
                "\n\nThank you for visiting The IYANI'S\' Hotel ")
    txt.insert(0.0, sentense)




tax=StringVar()
mytotal=StringVar()

lbltax=Label(root,text="Tax",font=('arial',16,'bold'),fg="firebrick")
lbltax.place(x=700,y=490)
taxentry=Entry(root,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT,textvariable=tax)
taxentry.place(x=850,y=490,width=350,height=30)
btotal=Button(root,text="Total",fg="firebrick",bg="dark olive green",font=('arial',18,'bold'),command=Total)
btotal.place(x=650,y=530,width=180,height=30)
totalentry=Entry(root,bg="deep sky blue",font=('arial',17,'bold'),justify=RIGHT,textvariable=mytotal)
totalentry.place(x=850,y=530,width=350,height=30)
print=Button(root,text="Print Receipt",fg="firebrick",bg="dark olive green",font=('arial',18,'bold'),command=printreceipt)
print.place(x=650,y=580,width=180,height=30)
reset=Button(root,text="Reset",fg="firebrick",bg="dark olive green",font=('arial',18,'bold'),command=Reset)
reset.place(x=850,y=580,width=180,height=30)
exit=Button(root,text="Exit",fg="firebrick",bg="dark olive green",font=('arial',18,'bold'),command=Exit)
exit.place(x=1020,y=580,width=180,height=30)

top.withdraw()
root.withdraw()
root.mainloop()