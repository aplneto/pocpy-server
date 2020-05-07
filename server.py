#!/usr/bin/env python3

import socket
import threading
from http_request import HTTPRequest

class HTTPServer(threading.Thread):
    def __init__(self, sock: socket.socket):
        self.__server_sock = socket
        self.alive = False
    
    def run(self):
        while True:
            pass
    
    def write_response(
    self,
    code = 200,
    status = "OK",
    version = "HTTP/1.1",
    encoding = "utf-8",
    headers = {
        "Server": "PocPy Server 1.0.0",
        "Content-Type": "text/html",
        "Length": "0"
    },
    body: bytes = None
    ):
        head = f"{version} {code} {status}"
        if body:
            headers["Length"] = len(body)
        response = head + '\n'.join(headers) + '\n\n'
        return response.encode() + body if body else bytes('')
    
    def kill_connection(self, client):
        pass

    def __call__(self, request: HTTPRequest):
        '''
        Method calls evaluates a request and directs it to the proper page
        method handler
        '''
        pass
    
    def require_authentication(self, method):
        '''
        This method should be used as a decorator to any page method that
        requires the user to be authenticated
        '''
        def verification(*args, **kwargs):
            pass
        return verification
    
    def get(self, method):
        '''
        This method should be used as a decorator to every method that handles
        a get request
        '''
        def decorator(*args, **kwargs):
            pass
        return decorator

class ClientResponser(threading.Thread):
    def __init__(self, client: socket.socket, parent: HTTPServer):
        threading.Thread.__init__(self)
        self.__client = client
        self.address = self.__client.getsockname()
        self.__parent = parent
        self.alive = False
        self.active_connections = []
    
    @property
    def location (self):
        return self.address[0]
    
    @property
    def port (self):
        return self.address[1]

    def run(self):
        while True:
            try:
                request = self.__client.recv(2**16)
            except:
                continue
            else:
                request_object = HTTPRequest.examine_request(request)
                response_body = self.__parent.get_page(request_object)
            
    def __bool__(self):
        return self.alive

def static_page(file_name: str):
    '''
    This method takes as argument a file path, opens it and returns it's
    byte content
    '''
    return open(file_name, 'rb').read()
    
def format_page(file_name: str, keywords: dict):
    '''
    This method takes a file path as argument, opens it and formats it
    using python's string format method and a dictionary containing the
    values that are supposed to be on the page.
    The placeholders should be written like python f-string placeholdes.
    eg.:
        <title>{title_Var}</title>
    '''
    return open(file_name, 'r').read().format(**keywords).encode("utf-8")