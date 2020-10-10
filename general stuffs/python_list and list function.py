# List

name = ["ram", "shayam", "gita", "sita"]
print(name)

# To print n element

print(name[2])


numbers = [4,1,2,4,9,19]
numbers.sort()
# Sort
print(numbers)

numbers.reverse()

print(numbers)


print(numbers[0:4])

# Extended Slice

print(numbers[::2])

# Functions of string
print(max(numbers))

print(min(numbers))

# Add element to list

numbers.append(99)
print(numbers)

# Add element to nth place

numbers.insert(1, 54)
print(numbers)

# Remove
numbers.remove(99)
print(numbers)

print(numbers.pop())


# Replace

numbers[1]=90
print(numbers)

# Mutable - can change
# Immutable - cannot change

###### Tuple

tp = (2,3,4)
# tp[1]=5 this will cause error because tuple is immutable
print(tp)

# For 1 elemnt tuple

tp1 = (1,)
print(tp1)

# Swap pyhton 

a=1
b=5
a,b =b,a
print(a,b)