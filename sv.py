import socket
import sys
import traceback
from threading import Thread
def main():
   start_server()
def start_server():
   host = "127.0.0.1"
   port = 8000 # arbitrary non-privileged port
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket created")
   try:
      soc.bind((host, port))
   except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()
   soc.listen(6) # queue up to 6 requests
   print("Socket now listening")
   # infinite loop- do not reset for every requests
   while True:
      connection, address = soc.accept()
      ip, port = str(address[0]), str(address[1])
      print("Connected with " + ip + ":" + port)
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
def clientThread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
    while is_active:
            client_input = receive_input(connection,max_buffer_size)
            if(client_input=='END'):
                data='Good bye'
                connection.sendall(data.encode())
                break
            else:
                try: 
                    data=switch(int(client_input))
                except:
                    data='Invalid'
            connection.sendall(data.encode())
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
