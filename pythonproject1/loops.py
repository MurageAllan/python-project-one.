# While loop illustration.
count = 1
while(count < 10):
    count = count + 2
    print(count)

# combination of else and while loop
count = 0
while(count < 10):
    count = count + 1
    print("Hello python.")
else:
    print("Hello good morning.")

# A program to print number 0 - 100
i = 0
j = 101
for i in range (0 , j):
    print(i)

# Mathematical table using for loop
num = 10
i =0
for i in range(1 , 11):
    print(num, 'x', i, '=', num * i)


num = 12
i = 0
for i in range(1, 11):
    ans = num * i
    print("{0} x {1} = {2}".format(num, i, ans))
