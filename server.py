import socket
import threading

class HTTPServer(threading.Thread):
    def __init__(self, sock: socket.socket):
        self.__server_sock = socket
        self.alive = False
        self.__sessions = {}
    
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