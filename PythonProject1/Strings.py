# strings can be enclosed by single or double quotes.
print("Today is a good day to learn python!")
print('My name is Nyamu Murage an aspiring software engineer and data engineer')

# string concatenation
print("Hello " + "world")

print()
# store strings in variables
greetings = "Hello"
name = input("Enter your name kindly") # The return value is the parameter entered in the input function.
print(greetings + " " + name)

# concatenate string with integers
age = 24
print("My age is " + str(age) + " years")

print()

print("My age is {0}" .format(age))

print("There are {0} days in the months of {1} , {2} , {3}".format(31, "jan", "Feb", "March"))

print("jan {2} feb {1}  march {0}"
      .format(30, 31, 28))
print("""jan {2} 
         feb {1} 
         march {0}"""
      .format(30, 31, 28))

for i in range(1, 13):
      print("No {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i ** 2, i ** 3))

for i in range(1, 13):
      print("No {0} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))








