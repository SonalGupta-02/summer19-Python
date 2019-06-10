#!usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
a=[]
b=[]
print("i) for storing no. greater than 5:--")
for i in adhoc:
	if i>5:
		print(i)
		a.append(i)
print("ii) for storing no. less than or equal to 2:--")
for i in adhoc:
	if i<=2:
		print(i)
		b.append(i)
print("List i) is:--",a)
print("List ii) is:--",b)