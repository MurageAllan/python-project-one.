name = input("Please enter your name.")
age = int(input("Please enter your age."))

if 18 <= age < 31:
    print(f"{name}  you are eligible to go for holiday kindly register!")
else:
    print("We are sorry {0} you cannot book with us for holiday.".format(name))