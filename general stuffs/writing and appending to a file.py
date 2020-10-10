f = open("myself.txt", "w")

f.write("My name is Divyanshu")  # writes from scratch

f.close()

# Append

f = open("myself.txt", "a")

f.write("My name is Divyanshu")

f.close()


# Find the number of characters written

f = open("boltuzamaki.txt", "w")

a = f.write("My name is Divyanshu")
print(a)
f.close()

## Read and Write file both

f = open("boltuzamaki.txt", "r+")
print(f.read())
f.write("This is written text")
f.close()