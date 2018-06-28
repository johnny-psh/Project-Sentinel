import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '23.95.9.251' # needs to be in quote
port = 8080
s.connect((host, port))


inpt = "select@select.com"
s.send(inpt)
print "the message has been sent"
output = s.recv(309)
print(output)
s.close()


