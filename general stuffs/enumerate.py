foods = ["samosa", "dosa", "chai", "biscuit", "pizza"]


# Long way
"""

i= 0 

for item in foods:
	if i % 2 is not 0:
		print(f"Buy me {item}")
		i  = i+1


"""


# This is short way
# enumerate return index and item both

for index, item in enumerate(foods):
	if index%2==0:
		print(f"Buy me {item}")

