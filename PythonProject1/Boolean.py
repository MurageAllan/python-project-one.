day = "Monday"
temperature = 30
raining = False
if ( day == "Monday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("You will go swimming tomorrow.")

if 0:
    print("True.")
else:
    print("False.")

name = input("Please enter your name ")
if name != "":
    print("The person's name is {0}".format(name))
else:
    print("The person has no name.")