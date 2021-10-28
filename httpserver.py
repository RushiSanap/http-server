#!/usr/bin/python
import sys
import time
from socket import *
from get import *
from head import *
from post import *
from put import *
from delete import *
from test import *
from headers import *

#start keyword will start the http server
#stop keyword will stop the http server
#restart keyword will stop and start the http server
'''
SERVER_MODE = sys.argv[1]
'''

class TCPServer:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    def start(self):
        #Method for starting the server
        s = socket(AF_INET, SOCK_STREAM)
        try:
            # assigns an IP address and a port number to a server socket
            s.bind((self.host, self.port))
        except OSError as e:
            print(e, "for", self.port)
            terminate_port(self.port)
            # s = socket(AF_INET, SOCK_STREAM)
            # s.bind((self.host, self.port))
        s.listen(5)

        print("Listening at......", s.getsockname())
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            #reading just the first 1024 bytes sent by the client.
            data = conn.recv(65536)
            response = self.handle_request(data.decode())
            conn.sendall(response)
            store_cookie(address=addr)
            conn.close()
    
    def stop(self):
        pass

    def restart(self):
        pass

    def handle_request(self, data):
        return data


class HTTPServer(TCPServer, Get, Head, Post, Put, Delete):

    def handle_request(self, data):
        # Handles incoming requests Get a parsed HTTP request
        request = HTTPRequest(data)

        try:
            # Call the corresponding handler method for the current request's method
            handler = getattr(self, '%s' % request.method)
            print(handler)
        except AttributeError:
            handler = self.HTTP_501_handler(request, data)
        
        response = handler(request, data)
        return response

class HTTPRequest:
    """Parser for HTTP requests.
    self.method: The current HTTP request method sent by client
    self.uri: URI for the current request
    self.http_version = HTTP version used by  the client
    """

    def __init__(self, data):
        try:
            lines = data.split('\r\n')
            requestLine = lines[0]  # request line is the first line of the data
            words = requestLine.split(' ')  # split request line into seperate words
            self.method = words[0] # call decode to convert bytes to string

            # we put this in if block because sometimes browsers don't send URI with the request for homepage
            if len(words) > 1:
                # call decode to convert bytes to string
                self.URI = words[1]

            # we put this in if block because sometimes browsers don't send HTTP version
            if len(words) > 2:
                self.http_version = words[2]
        except:
            self.method = None
            self.URI = None
            #default to HTTP/1.1 if request doesn't provide a version
            self.http_version = '1.1'
    
    #for extracting the useful information from the http request
    def parse(self, data):
        head = dict()

        lines = data.split('\r\n')
        lines = lines[1: len(lines)-2]
        for line in lines:
            splited = line.split(': ', 1)
            head.update({splited[0] : splited[1]})

        print(head)
        host = head.get('Host')
        user = head.get('User-Agent')
        acpt = head.get('Accept')
        acpt_enco = head.get('Accept-Encoding')
        conn = head.get('Connection')
       
        gen_hed = GeneralHeader(conn)
        req_hed = RequestHeader(host, user, acpt, acpt_enco)

        return gen_hed, req_hed

if __name__ == '__main__':
    server = HTTPServer()
    server.start()
