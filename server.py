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
    
    def kill_connection(self, client):
        pass