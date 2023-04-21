from tkinter import *
root = Tk()
root.geometry("600x700")
root.configure(bg = "pink")

firstname = Label(root, text="First name")
firstname.grid(row = 0, column = 0)

lastname = Label(root, text= "Last name")
lastname.grid(row = 1, column = 0)

age = Label(root, text="Age")
age.grid(row = 2, column = 0)

gender = Label(root, text="Gender")
gender.grid(row = 3, column = 0)

e1 = Entry(root)
e1.grid(row = 0, column=1)

e2 = Entry(root)
e2.grid(row = 1, column = 1)

e3 = Entry(root)
e3.grid(row = 2, column = 1)

e4 = Entry(root)
e4.grid(row = 3, column = 1)

town = Label(root, text="Town")
town.grid(row = 0, column= 2)

nationality = Label(root, text = "Nationality")
nationality.grid(row = 1, column = 2)

course = Label(root, text = "Course")
course.grid(row = 2, column=2)

duration = Label(root, text = "Duration")
duration.grid(row = 3, column= 2)

e5 = Entry(root)
e5.grid(row = 0, column= 3)

e6 = Entry(root)
e6.grid(row = 1, column= 3)

e7 = Entry(root)
e7.grid(row = 2,column= 3)

e8 = Entry(root)
e8.grid(row = 3,column= 3)

submit = Button(root, text = "submit",  padx=10, pady=10, bd = 5)
submit.grid(row = 7, column = 0)




root.mainloop()