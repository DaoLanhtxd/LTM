import socket
import sys
 

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 

host = 'localhost'
 

port = 8081

server_address = ((host, port))
 
print ("connecting")

stream_socket.connect(server_address)

message=''
while(message!='END'):
    message = str(input("Enter data: "))
    stream_socket.sendall(message.encode())
    data = stream_socket.recv(16)
    print (data.decode())
    
stream_socket.close()

