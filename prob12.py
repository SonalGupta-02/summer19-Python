#!/usr/bin/python3

import os
import pyqrcode
from pyqrcode import QRcode
from googlesearch import search

data=input("Enter the data to be searched:--")
l_url=[]
for i in search(data,stop=3):
	l_url.append(i)
	print(i)
j=0
for j in range(l_url):
	url=pyqrcode.create(l_url[j])
	n=open("qr_cd"+data+str(j)+".svg",'wb')
	url.svg(n,scale=8)
	j+=1
	
	
