import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '' 
port = 
s.connect((host, port))


inpt = "select@select.com"
s.send(inpt)
print "the message has been sent"
output = s.recv(309)
print(output)
s.close()


