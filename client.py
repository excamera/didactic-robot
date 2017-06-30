import socket
import sys

TCP_IP = "localhost" #sys.argv[1]
TCP_PORT = 12345
BUFFER_SIZE = 64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while(True):
    data = raw_input()
    s.send(data)
    if (data.lower() == 'quit'):
        s.close()
        break
    data = s.recv(BUFFER_SIZE)
    print 'received data: ', data
    if (data.lower() == 'quit'):
        s.close()
        break
