import socket
import sys
 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
 

port = 8081
 

sock.bind((host, port))

sock.listen(1)
 

print ('waiting for a connection')
connection, client = sock.accept()
 
print (client, 'connected')


print('Hello,IP:',client)
data=''
print(data)
while(data!='END'):
    data = connection.recv(16)
    if data:
        data=data.decode()
        if(data=='1'):
            data='one'
            connection.sendall(data.encode())
        if(data=='2'):
            data='two'
            connection.sendall(data.encode())
        if(data=='3'):
            data='three'
            connection.sendall(data.encode())
        if(data=='4'):
            data='four'
            connection.sendall(data.encode())
        if(data=='5'):
            data='five'
            connection.sendall(data.encode())
        if(data=='6'):
            data='six'
            connection.sendall(data.encode())
        if(data=='7'):
            data='seven'
            connection.sendall(data.encode())
        if(data=='8'):
            data='eight'
            connection.sendall(data.encode())
        if(data=='9'):
            data='nine'
            connection.sendall(data.encode())
        if(data=='END'):
            data='Good bye'
            connection.sendall(data.encode())
            break
    else:
        data='wrong data'
        connection.sendall(data.encode())

connection.close()
