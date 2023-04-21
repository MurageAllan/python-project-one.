shopping_list = ["computer", "Mouse", "Keyboard", "Monitor"]
another_List = shopping_list
print(id(shopping_list))
print(id(another_List))

shopping_list += ["Cookies"]
print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_List
print(a)

print("adding cream")
b.append("cream")
print(c)
print(d)