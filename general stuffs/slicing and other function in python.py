mystr = "My name is Divyanshu"

print(mystr[3])

# Output = n

print(mystr[0:4])

#output My n   



# Lenght of string

print(len(mystr))


# if we print index greater than len of string it prints all string and ignore rest

print(mystr[0:78])


# Print characters after skipping letters

print(mystr[0:5:2])  # Skkiping 2 chars

### 
print(mystr[:6])
# same as 
print(mystr[0:6])


# and similary [6:] is [6:18]


# Negative index
# Reverse string

print(mystr[::-1])

print(mystr[-4:-1])

# String functions

print(mystr.isalnum())  # only alphabet and numeric

print(mystr.endswith("shu"))   # check is it end with or not

print(mystr.count("u")) # count number of this characters

print(mystr.capitalize())

print(mystr.find("name"))  # find the starting string 

print(mystr.replace("is", "are"))