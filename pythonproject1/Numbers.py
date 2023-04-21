empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = even + odd
print(numbers)

print()

sorted_numbers = sorted(numbers)
print(sorted_numbers)

print()

digits = list("467222122") # returns a list of iterables in their initial order.
print(digits)

print()

dig = sorted("456282722") # returns a list of sorted iterables
print(dig)

print()

# more_numbers = list(numbers)
# more_numbers = numbers[:]        # copying a number through slicing
more_numbers = numbers.copy()  # Another way of copying a list.
print(more_numbers)
print(numbers is more_numbers)   # One list is not the other.
print(numbers == more_numbers)   # The two lists are the same.
# num = -262722 # Integer
# print(num)
#
# num = -0.37272 # float
# print(num)
#
# complex_number = complex(10 , 20) # complex number
# print(complex_number)