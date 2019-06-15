#!usr/bin/pyhton3

import  socket 
recv_ip="127.0.0.1"
recv_port=4444
  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))

  #Recieve data  from  sender  

while  4  >  2  :
    data=(s.recvfrom(100)) 
    print("Message from Sender:--",data[0].decode())
    
    #  reply to sender  
    print("--Reply to Sender msg--")
    rpl=input()
    s.sendto(rpl.encode(),data[1])
