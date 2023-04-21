from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")
text_Input = StringVar()
operator = ""

Tops = Frame(root, width= 1600, height=50,  bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width= 800, height= 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width= 300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

Lb1Info = Label(Tops, font=("arial", 50, "bold"), text="Restaurant Management System", fg="Steel Blue", bd=10, anchor="w")
Lb1Info.grid(row=0, column=0)

Lb1Info = Label(Tops, font=("arial", 20, "bold"), text=localtime, fg="Steel Blue", bd=10, anchor="w")
Lb1Info.grid(row=1, column=0)

#=============================================Calculator==============================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(12908, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicBurger = float(Chicken_Burger.get())
    CoCheese_Burger = float(Cheese_Burger.get())

    costofFries = CoF * 0.99
    costofDrinks = CoD * 1.00
    costofFilet = CoFilet * 2.99
    costofBurger = CoBurger * 2.87
    costofChicken_Burger =  CoChicBurger * 2.89
    costofCheese_Burger = CoCheese_Burger * 2.69

    costofMeal = "$", str("%.2f" % (costofFries + costofDrinks + costofFilet + costofBurger + costofChicken_Burger + costofCheese_Burger))

    payTax = ((costofFries + costofDrinks + costofFilet + costofBurger + costofChicken_Burger + costofCheese_Burger) * 0.2)

    TotalCost = (costofFries + costofDrinks + costofFilet + costofBurger + costofChicken_Burger + costofCheese_Burger)

    Ser_Charge = ((costofFries + costofDrinks + costofFilet + costofBurger + costofChicken_Burger + costofCheese_Burger) / 99)

    Service = "$", str("%.2f" % Ser_Charge)

    overAllCost = "$", str("%.2f" % (payTax + TotalCost + Ser_Charge))
    paidTax = "$", str("%.2f" % payTax)

    Service_Charge.set(Service)
    Cost.set(costofMeal)
    Tax.set(paidTax)
    SubTotal.set(costofMeal)
    Total.set(overAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set(" ")
    Fries.set(" ")
    Burger.set(" ")
    SubTotal.set(" ")
    Total.set(" ")
    Service_Charge.set(" ")
    Drinks.set(" ")
    Tax.set(" ")
    Cost.set(" ")
    Filet.set(" ")
    Chicken_Burger.set(" ")
    Cheese_Burger.set(" ")


txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right').grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="+", bg="powder blue",  command=lambda: btnClick("+")).grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="powder blue",  command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="powder blue",  command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction = Button(f2, padx=19, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="powder blue",  command=lambda: btnClick(1)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="x", bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear = Button(f2, padx=14, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="C", bg="powder blue", command=btnClearDisplay).grid(row=5, column=1)

btnEqual = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)

Division = Button(f2, padx=19, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)

#=================================Restaurant info 1============================================================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Filet = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()

Lb1Reference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w" )
Lb1Reference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), text=rand, bd=16, insertwidth=4, bg="powder blue", justify=RIGHT)
txtReference.grid(row=0, column=1)


Lb1Fries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries", bd=16, anchor="w" )
Lb1Fries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), text=Fries, bd=16, insertwidth=4, bg="powder blue", justify=RIGHT)
txtFries.grid(row=1, column=1)


Lb1Burger = Label(f1, font=('arial', 16, 'bold'), text="Burger Meal", bd=16, anchor="w" )
Lb1Burger.grid(row=2, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), text=Burger, bd=16, insertwidth=4, bg="powder blue", justify=RIGHT)
txtBurger.grid(row=2, column=1)


Lb1Filet = Label(f1, font=('arial', 16, 'bold'), text="Filet_o_Meal", bd=16, anchor="w" )
Lb1Filet.grid(row=3, column=0)
txtFilet = Entry(f1, font=('arial', 16, 'bold'), text=Filet, bd=16, insertwidth=4, bg="powder blue", justify=RIGHT)
txtFilet.grid(row=3, column=1)


Lb1Chicken = Label(f1, font=('arial', 16, 'bold'), text="Chicken_Meal", bd=16, anchor="w" )
Lb1Chicken.grid(row=4, column=0)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), text=Chicken_Burger, bd=16, insertwidth=4, bg="powder blue", justify=RIGHT)
txtChicken.grid(row=4, column=1)


Lb1Cheese = Label(f1, font=('arial', 16, 'bold'), text="Cheese_Meal", bd=16, anchor="w" )
Lb1Cheese.grid(row=5, column=0)
txtCheese = Entry(f1, font=('arial', 16, 'bold'), text=Cheese_Burger, bd=16, insertwidth=4, bg="powder blue", justify=RIGHT)
txtCheese.grid(row=5, column=1)

#============================Restaurant info 2 ======================================================
Lb1Drinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w" )
Lb1Drinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), text=Drinks, bd=16, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtDrinks.grid(row=0, column=3)


Lb1Fries = Label(f1, font=('arial', 16, 'bold'), text="cost of Meal", bd=16, anchor="w" )
Lb1Fries.grid(row=1, column=2)
txtFries = Entry(f1, font=('arial', 16, 'bold'), text=Cost, bd=16, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtFries.grid(row=1, column=3)


Lb1Burger = Label(f1, font=('arial', 16, 'bold'), text="Service charge", bd=16, anchor="w" )
Lb1Burger.grid(row=2, column=2)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), text=Service_Charge, bd=16, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtBurger.grid(row=2, column=3)


Lb1Filet = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor="w" )
Lb1Filet.grid(row=3, column=2)
txtFilet = Entry(f1, font=('arial', 16, 'bold'), text=Tax, bd=16, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtFilet.grid(row=3, column=3)


Lb1Chicken = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w" )
Lb1Chicken.grid(row=4, column=2)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), text=SubTotal, bd=16, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtChicken.grid(row=4, column=3)


Lb1Cheese = Label(f1, font=('arial', 16, 'bold'), text="Total cost", bd=16, anchor="w" )
Lb1Cheese.grid(row=5, column=2)
txtCheese = Entry(f1, font=('arial', 16, 'bold'), text=Total, bd=16, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtCheese.grid(row=5, column=3)

#==============================================Buttons=======================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total", bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit", bg="powder blue", command=qExit).grid(row=7, column=3)









root.mainloop()

