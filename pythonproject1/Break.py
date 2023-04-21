str = "python"
for i in str:
    if i == "o":
      break
    print(i)

print()

i = 0
while 1:
    print(i, " ", end=" ")
    i = i +1
    if i == 10:
        break
print("Come out of the loop.")

print()

for i in range(100):
    print(i)
    if i ==  56:
        break

print()

num = 0
for i in range(50):
    num += 1
    if num == 20:
        break
    print("The number has value", num)
print("Out of the loop")


print()


n = 2
while 1:
    i = 1
    while i < 10:
        print("%d x %d = %d\n" %(n, i, n * i))
        i = i + 1
    choice = int(input("Do you want to continue printing the table? "))
    if choice == 0:
        break
    n = n + 1
