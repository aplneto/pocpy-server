import socket
import threading
from site_tree import WebPage
from http_request import HTTPRequest

class ClientResponser(threading.Thread):
    def __init__(self, client: socket.socket, index: WebPage):
        threading.Thread.__init__(self)
        self.__client = client
        self.address = self.__client.getsockname()
        self.index = index
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
                response_body = self.__parent(request_object)
            
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