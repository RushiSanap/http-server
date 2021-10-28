#!/usr/bin/python
import gzip
from socket import *
#import pdb;pdb.set_trace()
s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1", 8888))
print('done connection')

message = "GET /home/ubuntu/http-server/httpserver.py HTTP/1.1\r\n"
message += "HOST: 127.0.0.1:8888\r\n"
#message += "User-Agent: Firefox/86\r\n"
message += "\r\n"
x = s.send(message.encode())
data = s.recv(65536)

# print(data.decode())
i = data.index(b"\r\n\r\n")
print(data[:i+3].decode())
data = data[i+4:]
print(gzip.decompress(data).decode())