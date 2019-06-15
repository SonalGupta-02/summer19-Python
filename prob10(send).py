#!usr/bin/python3

import socket
rec_ip='127.0.0.1'
rec_port=7777

print("1.To send/recieve meassages from both sides.. \n 2.To send msg from sender and recieve it through reciever..")

s=s.socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
choice=input("Enter your choice:--")

while True:
	if choice == '1':
		msg=input("Enter message:--")
		s.sendto(msg.encode('ascii'),(rec_ip,rec_port))
		data=s.recvfrom(100)
		n_data=data[0].decode('ascii')
		print("Message:-",data)
	if choice == '2':
		msg=input("Enter message:--")
		s.sendto(msg.encode('ascii'),(rec_ip,rec_port))
