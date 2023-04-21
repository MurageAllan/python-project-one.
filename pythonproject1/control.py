maths = float(input("Enter the maths marks: "))
english = float(input("Enter the english marks: "))
swahili = float(input("Enter the swahili marks: "))
biology = float(input("Enter the biology marks: "))
total = maths + english + swahili + biology
print("The total marks are : ", total)
average = total / 4
print("The average is :", average)

if 100 <= average >= 85:
    print("Grade A")
elif 84.99 <= average >= 60:
    print("Grade B+")
elif 59.99 <= average >= 40:
    print("Grade B")
elif 39.99 <= average >= 30:
    print("Grade C")
elif 29.99 <= average >= 20:
    print("Grade D")
else:
    print("Grade E")
