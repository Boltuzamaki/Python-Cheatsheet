s = set()

s_from_list = set([3,4,1,9,0])
print(s_from_list)
print(type(s_from_list))

s_from_list.add(45)
print(s_from_list)

s1 = set()

s1.add(1)
s1.add(2)

s1.union({1,2})
print(s1)

s2 = s1.intersection({1,3})
print(s2)

# remove 

s1.remove(1)