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
   data = soc.recv(5120)
   print (data.decode())
   if(data.decode()=='429 Too Many Requests'):
      soc.close()
   else:
      print("Please enter 'END'to exit")
      message=""
      while(message!='END'):
          message = str(input("Enter data: "))
          soc.sendall(message.encode())
          data = soc.recv(5120)
          print (data.decode())
      soc.close()
if __name__ == "__main__":
   main()
