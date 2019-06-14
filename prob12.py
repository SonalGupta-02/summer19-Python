#!/usr/bin/python3

import os
import pyqrcode
import webbrowser
from pyqrcode import QRcode
from googlesearch import search

data=input("Enter the data to be searched:--")
l_url=[i for i in search(data,stop=3)]

for i in range(l_url):
	url=pyqrcode.create(l_url[i])