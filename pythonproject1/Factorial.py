num = 7

factorial = 1

if num < 0:
    print("Sorry factorial of a number does not exist.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
        print(factorial)


def Factorial(x):
    if x == 1:
        return  1
    else:
        return  (x * factorial(x - 1))


number = int(input("Please enter a number."))
result = Factorial(number)
print(result)