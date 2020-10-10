list1 = ["samosa", "dosa", "chat", "paapaad"]

for l in list1:
	print(l)


lists = [['samosa', 4], ["dosa",5], ["chat", 2], ["pakoda", 4] ]

for food, count in lists:
	print(food, count)


# lists can be directly convert to dictionary

dict1 = dict(lists)
print(dict1)

for food, count in dict1.items():
	print(food, count)