# Slicing backwards the start no should be greater than the stop then use a negative step.
letters ="abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

last_Eight = letters[25:25-8:-1]
print(last_Eight)

last_four = letters[-4:]
print(last_four)