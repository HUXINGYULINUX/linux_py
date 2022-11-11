import socket
import os
def sendfile(conn):
	str1 = conn.recv(1024)
	filename = str1.decode('utf-8')
	print('The sever requests my file:',filename)
	if os.path.exists(filename):
		print('Hello, I have %s,begin to upload'% filename)
		conn.send(b'yes')
		conn.recv(1024)
		size = 1024
		with open(filename,'rb') as f:
			while True:
				data = f.read(size)
				conn.send(data)
				if len(data)<1024:
					break
		print('%s is upload successfully!' % filename)
	else:
		print('Sorry,I have not %s' % filename)
		conn.send(b'no')
	conn.close()
s = socket.socket()
s.connect(('127.0.0.1',1234))
while True:
	sendfile(conn)