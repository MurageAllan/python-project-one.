pangram = "The quick brown fox jumps over the lazy dog."
letter = sorted(pangram, key= str.casefold) # Enables sorting without effect of upper case leteres.
print(letter)

print()

numbers = [1.2, 4.3, 7.4, 3.4, 9.8, 3.5, 4.9, 8.0]

print()

sorted_numbers = sorted(numbers)    # sorted() creates a new list of numbers.
print(sorted_numbers)
print(numbers)

print()
numbers.sort() # sort() sorts without creating a new list of numbers.
print(numbers)

print()

names = ["Graham", "John", "erick", "mark", "Ian", "Duncan"]
names.sort(key= str.casefold)
print(names)