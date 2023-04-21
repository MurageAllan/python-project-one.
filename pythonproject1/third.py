# Check whether a number is even
num = int(input("Enter a number : "))
if num % 2 == 0:
    print("The number is even.")

a = int(input("Enter number a "))
b = int(input("Enter number b "))
c = int(input("Enter number c "))

# Check of the three numbers a , b , c which is the greatest.
if a > b and a > c:
    print("The largest number that is a is ", a)
elif b > a and b > c:
    print("The largest number that is b is ", b)
else:
    print("The largest number that is c is ", c)

# Check of the three numbers a , b , c which is the smallest
if a < b and a < c:
    print("The smallest number that is a is ", a)
elif b < a and b < c:
    print("The smallest number that is b is ", b)
else:
    print("The smallest number that is c is ", c)

# Check whether a number is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number entered is even ")
else:
    print("The number is odd.")

marks = float(input("Enter grade marks"))

if 100 >= marks >= 85:
    print("Grade A")
elif 84.99 >= marks >= 60:
    print("Grade B+")
elif 59.99 >= marks >= 40:
    print("Grade B")
elif 39.99 >= marks >= 30:
    print("Grade C")
elif 29.99 >= marks >= 20:
    print("Grade D")
else:
    print("Grade E")
