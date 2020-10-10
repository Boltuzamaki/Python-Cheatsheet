# Built in function
a = 1 
b = 3

print(sum((a,b)))

# Self made function 
def printname():
	print("Hello my name is Divyanshu")

printname()

# Print average
# Doc string
def average_fun(a,b):
	"""This function prints the average of two numbers"""
	return(a+b/2)

print(average_fun(4,3))
print(average_fun.__doc__)