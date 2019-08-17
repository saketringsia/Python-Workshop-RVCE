key = 0
key = int(input("Enter Choice"))
if(key==1):
	n = int(input("Enter a number:"))
	rev = 0
	while(n>0):
		rem = n%10
		rev = rev * 10 + rem
		n=n//10
	print(rev)
elif(key==2):
	for i in range(4):
		for j in range(i):
			print("*",end = " ")
		print("\n");
else:
	print("GoodBYE! We will move on to Applications")
