s=input("")
vowe=['a','e','i','o','u','A','E','I','O','U']
y=0
for x in s:
	if x in vowe:
		y=1
if(y==1):
	print("yes")
else:
    print("no")
