import socket
import os
s = socket.socket()
s.bind(('127.0.0.1',1234))
s.listen(2)  # 监听
print('waiting for connecting...')
conn, addr = s.accept()  # 等待连接
while True:
	filename = 'D:/upload/myfirst.docx'
	print('I want to get the file %s!'% filename)
    s.send(filename.encode('utf-8'))
    str1 = s.recv(1024)
    str2 = str1.decode('utf-8')
    if str2 == 'no':
    	print('the file %s not exit'% filename)
    else:
    	s.send(b'I am ready!')
    	temp = filename.split('/')
    	myname = 'my_'+temp[len(temp)+1]
    	size = 1024
    	with open(myname,'wb') as f:
    		data = s.recv(size)
    		f.write(data)
    		if len(data)<size:
    			break
    	print('The upload file is %s.'% filename)
s.close()		