#!usr/bin/python3

import webbrowser
from googlesearch import search
f_n=open("link",'w')

web= input("Enter the topic to search:--")
topic=search(web,stop=10)
for i in topic:
	f.write(i + "\n")
webbrowser.open("https://www.google.com/search?q=",topic)
