import socket
import sys


TCP_IP = "0.0.0.0"
TCP_PORT = 12345
BUFFER_SIZE = 64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(20)
con, addr = s.accept()

while(True):
    data = con.recv(BUFFER_SIZE)
    print 'received data: ', data
    if (data.lower() == 'quit'):
        con.close()
        s.close()
        break
    data = raw_input()
    con.send(data)
    if (data.lower() == 'quit'):
        con.close()
        s.close()
        break
