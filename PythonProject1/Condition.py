age = int(input("How old are you ?"))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16, 66):
    print("you are old enough.")
else:
    print("Enjoy your free time.")

print("_" * 80)

if age < 16 or age > 65:
    print("enjoy your free time")
