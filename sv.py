import socket
import sys
import traceback
import codecs
import urllib.request
import shutil
from threading import Thread
def main():
   start_server()
def start_server():
   host = "127.0.0.1"
   port = 8000 # arbitrary non-privileged port
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket created")
   arr=[]
   try:
      soc.bind((host, port))
   except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()
   soc.listen(6) # queue up to 6 requests
   print("Socket now listening")
   print("Sever IP: "+host+" port: "+str(port))
   file=open("online.log","w+")
   file.close()
   # infinite loop- do not reset for every requests
   while True:
      test=1
      file=open("online.log","r+")
      connection, address = soc.accept()
      ip, port = str(address[0]), str(address[1])
      count=0
      while True:
         line=file.readline()
         line=line.replace("\n","")
         if not line:break
         else:
            count=count+1
            if(line==ip):
               data=("429 Too Many Requests")
               connection.sendall(data.encode())
               f1=open("access.log","w")
               f1.write(ip+"\t"+port+"\t"+"429 Too Many Requests\n")
               f1.close()
               connection.close()
               test=0
      if(count>=10):
         data=("503 Service Unavailable")
         connection.sendall(data.encode())
         f1=open("access.log","w")
         f1.write(ip+"\t"+port+"\t"+"503 Service Unavailable\n")
         f1.close()
         connection.close()
         test=0
      file.close()
      if(test==1):
         print("Connected with " + ip + ":" + port)
         file=open("online.log","w")
         file.write(ip+"\n")
         data=("Connected")
         connection.sendall(data.encode())
         file.close()
         try:
            Thread(target=clientThread, args=(connection, ip, port)).start()
         except:
            print("Thread did not start.")
            traceback.print_exc()
   soc.close()
def switch(i):
        switcher={               
                1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine'
             }
        return switcher.get(i,'Invalid')
def clientThread(connection, ip, port, max_buffer_size = 51200):
    is_active = True
    while is_active:
            client_input = receive_input(connection,max_buffer_size)
            if(client_input=='END'):
                data='Good bye'
                connection.sendall(data.encode())
                break
            else:
               if(client_input.startswith("dig",0,3)and client_input.startswith(".com",len(client_input)-4,len(client_input))and len(client_input.split(" "))==2):
                  arr=client_input.split(" ")
                  HostName=arr[1]
                  data=socket.gethostbyname(HostName)
               else:
                  if(client_input.startswith("curl",0,4)and client_input.startswith("http://",5,13)and len(client_input.split(" "))==2):
                     arr=client_input.split(" ")
                     link=str(arr[1])
                     f = open("a.html", "wb")
                     code = urllib.request.urlopen(link)
                     shutil.copyfileobj(code, f)
                     ff=codecs.open('a.html','r')
                     data=ff.read()
                     print(data)
                  else:
                      try: 
                          data=switch(int(client_input))
                      except:
                          data='Invalid'
            connection.sendall(data.encode())
    file=open("access.log","w")
    file.write(ip+"\t"+port+"\t"+"Closed by Client\n")
    file.close()
    arr=[]
    file=open("online.log","r+")
    while True:
         line=file.readline()
         line=line.replace("\n","")
         if not line:break
         else:
            arr.append(line)
    file.close()
    arr.remove(ip)
    file=open("online.log","w")
    for i in arr:
         file.write(i+"\n")
    file.close()
    connection.close()
def receive_input(connection, max_buffer_size):
   client_input = connection.recv(max_buffer_size)
   client_input_size = sys.getsizeof(client_input)
   if client_input_size > max_buffer_size:
      print("The input size is greater than expected {}".format(client_input_size))
   decoded_input = client_input.decode("utf8").rstrip()
   return decoded_input
if __name__ == "__main__":
   main()
