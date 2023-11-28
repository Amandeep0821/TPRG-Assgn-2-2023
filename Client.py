# runs on Pi
#AMANDEEP SINGH
#100893335

import socket
s = socket.socket()
host = '10.102.13.145'
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()