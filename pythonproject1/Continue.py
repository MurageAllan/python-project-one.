str = "Python"

for char in str:
    if char == "o":
        continue
    print(char)

i = 0
while 1:
    print(i, " ", end=" ")
    i = i + 1
    if i == 10:
        continue
    print(i)