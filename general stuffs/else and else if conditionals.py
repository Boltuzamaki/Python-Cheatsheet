var1 = 4

var2 = int(input())

if var2>var1:
	print("Yes")
else:
	print("No")


# If we dont want to check all if statement try elif

var1 = 4

var2 = int(input())

if var2>var1:
	print("Greater")
elif var2==var1:
	print("Equal")
else:
	print("Lesser")


l = [2,3,4,5]

if 2 in l:
	print("yes it is")

if 22 not in l:
	print("Yes")