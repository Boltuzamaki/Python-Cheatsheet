def animal(a, b, c, d):
	return a,b,c,d



print(animal("cow", "dog", "cat", "monkey"))

# If we have to add multiple name continuosly we can't write a,b,c,d blah blah forever 

# Use args

def animal(*args):
	for item in args:
		print(item)
# Fedd any numbers of input 

# It feeded as a tuple
names= [ "cow", "dog", "cat", "monkey","girrafe"]
animal( names)


def allinone(normal, *args, **kwargs):
	print(normal)
	for item in args:
		print(item)
	print(args)
	for key, value in kwargs.items():
		print(f"{key} eats {value}")


name_food = {"ram":"dosa","gita":"samosa","shyam":"rasogulla"}
animal = ["cow", "dog"]

allinone("This is the overall test", *animal , **name_food )