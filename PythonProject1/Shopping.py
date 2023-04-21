shopping_List = ["Milk", "Pasta", "eggs", "spam", "bread", "rice"]

# for items in shopping_List:
#     if items != "spam":
#         print("Buy " + items)

for items in shopping_List:
     if items == "spam":
         continue
     print("Buy " + items)

for items in shopping_List:
     if items == "spam":
         break
     print("Buy " + items)