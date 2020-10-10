# Map 

# If we want to run my function on a numbers of element in list

numbers = ["23", "12", "90", "13", "11"]

""" Normal way 
# If we want to conevert all number as int
for num in range(0, numbers):
	numbers[num] = int(numbers[num])

"""

# Map way
numbers = list(map(int, numbers))

print(numbers[1]+ 1)

# Print square ez
