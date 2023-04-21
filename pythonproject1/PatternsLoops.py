rows = 7
for i in range(rows):
    for j in range(i):
        print(i, end=" ")
    print('')

print()

rows = 5
for i in range(1, rows + 1):
    for i in range(1, i + 1):
        print(i, end='  '  )
    print(' ')

print()

# Inverted numbers
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end='')
    print('\r')

print()

rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end='')
    print("\r")
