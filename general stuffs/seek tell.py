f = open("file.txt")

# Tells the index of the chracters

print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())

f.close()



##### Seek helps to reset the readline to the caharcter want

f = open("file.txt")

print(f.readline())

f.seek(4)

print(f.readline())