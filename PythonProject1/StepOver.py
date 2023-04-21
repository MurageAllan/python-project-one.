# number = "9,223;372:036 854,775;807"
number = input("Please enter a string of numbers separators separated using separators of your choice.")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))