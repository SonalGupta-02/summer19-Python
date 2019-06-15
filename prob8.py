#!usr/bin/python3

import os
import sys
from shutil import which
cmnd=input()
while(cmnd) :
	f_n=open("comandlist",'a+')
	f_n.write(com)
	for i in f_n :
		if(cmnd == i) :
			print("REPEATED COMMAND")
			cmnd=input() 
		if(which(cmnd)) :
			os.system(cmnd)
		elif(cmnd == "exit") :
			sys.exit(0)		
		else :
			print("Command not found!!")
			cmnd=input()