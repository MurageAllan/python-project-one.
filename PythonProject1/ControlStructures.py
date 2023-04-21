name = input("What is your name ?")
age = int(input("How old are you {0} ? " .format(name)))
print(age)

# if age >= 18:
#     print("The person is eligible to vote.")
#     print("Please put an x on the ballot paper.")
# else:
#     print("The person is not eligible to vote.")

if age < 18:
    print("Come back after {0} years".format(18 - age))
elif age == 900:
    print("Sorry you should not exist.")
else:
    print("The person is allowed to vote.")