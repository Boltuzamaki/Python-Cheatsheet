# Lmabda function or anonymous function

def add(a,b):
	return a+b


minus = lambda x,y:x-y

# Same as

"""def minus(x,y):
	return x-y"""

print(minus(9,4))


# Other example

print("Other example")

a = [[1,4], [2,1], [4,10], [1,2]]

def a_first(a):
	return a[1]

a.sort(key = a_first)

print(a)

print("Using lambda function")

a.sort(key =  lambda x:x[1])
print(a)