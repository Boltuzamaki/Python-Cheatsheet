foods = ["chat", "samosa", "dosa", "pakora", "pizza", "burger"]


# way 1 

print("Way 1 ")
for item in foods:
	print(f"{item}", "and", end=" ")


print("\nWay 2 ")

a = " and ".join(foods)    # Put anything instead of and with you want to join

print(a)

