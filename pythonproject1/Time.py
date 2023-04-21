import time
import datetime
import calendar
from datetime import date


print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(datetime.datetime.now())

s = calendar.prcal(1700)

print()

yy = int(input("Enter the year : "))
mm = int(input("Enter the month : "))
print(calendar.month(yy,  mm))

print()

date1 = datetime.date.today()
print(date1)

print()

today = date.today()
print("The current date = ", today)

print()

timeStamp = date.fromtimestamp(132626467)
print("Date = ", timeStamp)



