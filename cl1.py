import socket
import sys
def main():
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "127.0.0.1"
   port = 8000
   try:
      soc.connect((host, port))
   except:
      print("Connection Error")
      sys.exit()
   data = soc.recv(51200)
   print (data.decode())
   if(data.decode()=='429 Too Many Requests'):
      soc.close()
   else:
      print("Please enter 'END'to exit")
      message=""
      while(message!='END'):
          message = str(input("Enter data: "))
          soc.sendall(message.encode())
          data = soc.recv(51200)
          if(message.startswith("curl",0,4)and message.startswith("http://",5,13)and len(message.split(" "))==2):
            f = open("link.html", "wb")
            f.write(data.decode().encode('utf-8'))
            f.close()
          else:
             print (data.decode())
      soc.close()
if __name__ == "__main__":
   main()
