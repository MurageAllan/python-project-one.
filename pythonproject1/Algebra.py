
def Fibonacci(n):
    if n < 0:
        print("Incorrect input.")
    elif n == 0:
        return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(6))


number = int(input("How many times? "))
number1 = 0
number2 = 1
count = 0
if number <= 0:
    print("Please enter a positive number")
elif number == 1:
    print("The fiboncci of the numbers ", number, ":")
    print(number1)
else:
    print("The fibonacci of the sequence is: ")
    while count < number:
        print(number1)
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1