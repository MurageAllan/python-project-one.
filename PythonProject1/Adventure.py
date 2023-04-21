available_exits = ["east", "west", "south", "north"]

chosen_exist = ""

while chosen_exist.casefold() not in available_exits:
    chosen_exist = input("Please choose a direction: ")
    if chosen_exist.casefold() == "quit":
        print("Game over!")
        break

print("Aren't you glad you have chosen the right direction.")