# result = True
# another_result = result
# print(id(result))
# print(id(another_result))

result = "correct"
another_result = result
print(id(result))
print(id(another_result))

result  = result + "ish"
print(id(result))
print(id(another_result))