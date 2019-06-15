#!/usr/bin/python3

import socket
rec_ip='127.0.0.1'
rec_port=7777

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rec_ip,rec_port))
choice=input()
while True:
	if choice == '1':
		data=s.recvfrom(100)
		n_data=data[0].decode('ascii')
		print("Data from Sender:--",n_data)
		reply=input("Your Reply:--")
		s.sendto(reply.encode('ascii'),data[i])
	if choice == '2':
		data=s.recvfrom(100)
		n_data=data[0].decode('ascii')
		print("Data form Sender:--",ndata)

s.close()