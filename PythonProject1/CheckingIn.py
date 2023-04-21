parrot = "Norwegian blue"
letter = input("Enter the char.")
if letter in parrot:
    print("{0} is in {1}".format(letter, parrot))
else:
    print("I don't need that letter.")
