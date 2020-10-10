
import time
initial = time.time()
for i in range(45):
	print("This is it")

print("For loop time", time.time()- initial, "Seconds")

initial1 = time.time()
k = 0
while (k<45):
	print("This is it")
	k=k+1

print("While loop time", time.time()- initial1, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)