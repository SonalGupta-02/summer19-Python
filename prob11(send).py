#!usr/bin/python3

import  socket 
recv_ip="127.0.0.1"
recv_port=4444 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1 < 2 :
	msg=input("Enetr your Message:--- ")
	if len(msg) < 150:  
		s.sendto(msg.encode(),(recv_ip,recv_port)) 

     #Recieve data  from  reciever
		print(s.recvfrom(100))
		print("REPLY FROM RECEIVER:---")
	else :
		print("ENTER MSG WITHIN 150 CHAR")	
