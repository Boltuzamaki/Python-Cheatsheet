# Try to run code if error the print in except or run some other code


print("Enter num 1")
num1 = input()

print("Enter num 2")
num2 = input()

try:
	print("The sum of number is", int(num1)+int(num2))

except Exception as e:
	print(e)