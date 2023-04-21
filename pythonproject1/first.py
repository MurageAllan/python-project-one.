pi = 3.142
length = int(input("Enter the length: "))
area = pi * length * length
print(area)


num = int(input("Enter the number: "))
squareRoot = num ** 0.5
print(squareRoot)


num = int(input("Enter the number: "))
cubeRoot = num ** (1./3.)
print(cubeRoot)


amount = int(input("Enter the amount amount: "))
rate = int(input("Enter the annual rate: "))
time = int(input("Enter the time in years: "))
interest = (amount * rate * time) / 100
print(interest)
