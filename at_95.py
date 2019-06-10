#!usr/bin/python3

import datetime

name=input("Enter your name:--")
age=int(input("Enter your age:--"))

at_95=(datetime.datetime.now().year)

print(name,"will be 95 yrs old in the year:-",at_95+(95-(age)))