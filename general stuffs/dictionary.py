d1 = {}

print(type(d1))

# keys and value pair

d1 ={"divyanshu":2017317, "abhi":201730, "sajal":2017342, "food":{"samosa":4, "dosa":5, "chat":3}}

print(d1["divyanshu"])

print(d1["food"])

# add elemet
d1["anonymus"] = 2017900
print(d1)

del(d1["abhi"])

print(d1)

#add element via update

d1.update({"sweet":"rasogulla"})
print(d1)

# Print all keys

print(d1.keys())

# items

print(d1.items())