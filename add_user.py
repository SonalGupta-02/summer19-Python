#!usr/bin/python3

import os
import crypt

f=0
uname=input("Enter username:--")
for i in uname:
	if i.isdigit():
		f=1
if f == 1:
	print("Invalid")
elif f == 0:
	pswd="hello"+uname
	epass = crypt.crypt(pswd,"22")
	os.system("useradd -p "+ epass +"  "+uname)
	print("User Added..")	