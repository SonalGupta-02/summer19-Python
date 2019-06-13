#!usr/bin/python3

print("1.To print the data of single file \n 2.To print the data of Multiple files")

choice=int(input("Enter ypur choice:--"))
if choice == '1':
	f_name=input("Enter file name:--")
	fnew=open(f_name,'r')
	print(fnew.read())
	fnew.close()
elif choice == '2':
	num=int(input("Enter no of files:"))
	l=[]
	for i in range(num):
		file_l=input("Enter file name")
		l.append(file_l)
		print(l)
	for i in l:
		f=open(i,'r')
		print('\n')
		print(f.read())
		
	
