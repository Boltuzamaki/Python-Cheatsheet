# Break helps to come out of loop
# Continue helps to forget all statement below this command
i=0
while(True):
	if i<5:
		i=i+1
		continue     # After contune runs it not go further

	if i>45:
		break
	i=i+1
	print(i)


# Input example



while(True):
	num = int(input())
	if num == 47:
		break
	else:
		continue