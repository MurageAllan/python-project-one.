parrot = "Norwegian blue"

print(parrot[0:6:3])
print(parrot[0:6:2])

print(parrot)
print(parrot[3]) # prints the forth char.

print()

print(parrot + "\n" + parrot[3] + "\n" + parrot[4] + "\n" + "\n" + parrot[3] + "\n" + parrot[6] + "\n" + parrot[8])
print()

print(parrot)
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot[0:6]) # slicing from position 0 to the sixth char not including it.
print(parrot[3:6])


print(parrot[0:9])
print(parrot[:9])
print(parrot[-14:-5])

print()
print(parrot[10:14])
print(parrot[10:])
print(parrot[-4:])
print()
print(parrot[:9] + " " + parrot[10:])
print(parrot[:])


print()
numbers = "9,223;372:036 854,775;807 "
print(numbers[1::4])