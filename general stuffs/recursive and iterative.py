# Recursive approach

def factorial(num):
	if num<1:
		return 1
	else:
		return  factorial(num-1)*num
      

print(factorial(4))


# Iterative approach

def factorial2(num):
	r = 1
	for i in range(1, num+1):
		r = i*r
	return r 	
print(factorial2(4))


# Fibonacci 

def fibonaaci(num):
	lists = []
	if num == 1:
		return 0
	elif num == 2:
		return 1 
	else:
		return fibonaaci(num-1) + fibonaaci(num-2)

print(fibonaaci(7))


# Iterative

def iter_fibonnaci(num):
	a = 0
	b = 1
	temp = 0
	counter = 0
	if num == 1:
		return 0
	elif num == 2:
		return 1
	else:
		while (counter < num-2):
			temp = a + b
			a = b
			b = temp

			counter = counter + 1 

		return temp
print(iter_fibonnaci(10))