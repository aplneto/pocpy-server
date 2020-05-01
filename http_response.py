class HTTPResponse (object):
    def __init__(self, code: int, headers: dict, body = None):
        self.__code = code
        self.headers = headers
        self.body = body
    
    def add_header(self, title: str, value: str):
        self.headers[title] = value