'''print(3+4)
a=10
print(a)'''
'''cond=1
while cond <10:
	print(cond)
	cond+=1'''
'''while True:
	print('gujjar')'''
'''list = [7,8,9]
for each_number in list:
	print(each_number)'''
'''for a in range(1,1000):
	print(a)'''
'''text ='gujjar ka bhai pandat'
saveFile = open('bro.txt','w')
saveFile.write(text)
saveFile.close'''
'''appendMe = 'chocobar bhabhiji'
appendFile = open ('bro.txt','a')
appendFile.write(appendMe)
appendFile.close'''
'''readMe = open('bro.txt','r').readlines()
print(readMe)'''
'''xyz = raw_input('bhabhi ji kaisi hain')
print(xyz)'''
'''import Example
Example.fun('test')'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (s)
server = 'amazone.net'
port = 80
server_ip = socket.gethostbyname(server)
print(server_ip)

