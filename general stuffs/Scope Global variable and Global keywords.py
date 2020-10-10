num = 4 # Global scope
num1 = 5

def function1():
	print(num)
function1()
print(num)

# output 
# 4
# 4

def function2():
	global num
	print(num)
	num =8
	print(num)

function2()

# Output 1 becuase local is moreimportant for function
# Output 4 4 4 8