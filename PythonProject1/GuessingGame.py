import random


highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: REMOVE AFTER TESTING.
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done you got it.")
        break
    else:
        if guess < answer:
            print("Please guess higher.")
        else:
            print("Please guess lower.")
            guess = int(input())
# if guess == answer:
#     print("Well done you got it right the first time.")
# else:
#     if guess < answer:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you got it.")
#     else:
#         print("You have not guessed correctly.")






# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("You are correct you guessed it.")
#     else:
#         print("Sorry you did not guessed correctly.")
# elif guess > answer:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("You are correct you guessed it.")
#     else:
#         print("Sorry you have not guessed correctly.")
# else:
#     print("You got the answer.")

