#!usr/bin/pyhton3

import datetime

hr=int((datetime.datetime.now().strftime(%H)))

if hr<=12:
	print("Good Morning!!")
elif hr>12 and hr<=17:
	print("Good AfterNoon!!")
elif hr>17 and hr<=22:
	print("Good Evening!!")
else:
	print("Good Night!!")