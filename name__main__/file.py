## __name__ == "__main__" only if the function is run from tat file 
# If run from other file then name changes
# Suppose we call this file from other file without __name__=="__main__"
# Then taht file will print stuffs of this fie too

def func1():
	return "my name is boltuzamaki"


def add(a,b):
	return (a,b)

## So we use __name__=="__main__"

print(__name__)
if __name__=="__main__":
	print(func1())
	print(add(1,2))