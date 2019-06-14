#!/usr/bin/python3

import os
import pyqrcode
import webbrowser
from pyqrcode import QRcode
from googlesearch import search

data=input("Enter the data to be searched:--")
l_url=[i for i in search(data,stop=3)]
f_name=open('var/www/html/qr_code.html','w')
for i in range(l_url):
	url=pyqrcode.create(l_url[i])
	n=open("var/www/html"+data+str(i)+".svg",'wb')
	url.svg(n,scale=8)
	
