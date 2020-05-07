import re

class HTTPRequest(object):
    URL = r"([a-zA-Z\.\+\-]+://)" \
    r"([a-zA-Z0-9_\-\+\.]+:[a-zA-Z0-9_\-\+\.]*@)?" \
    r"([a-zA-Z0-9\-]{1,63}\.?)+" \
    r"(:\d{1-5})?" \
    r"(/(\w*)?)*" \
    r"(\?(\w*=\w*&?)*)?"

    def __init__(
        self, method: str, path: str, version: str, headers = [],
        params = [], body = None
    ):
        self.__method = method
        self.__path = path
        self.__version = version
        self.__headers = headers
        self.__params = params
        self.__body = body

    @staticmethod
    def examine_request(request: bytes, encoding = 'utf-8'):
        '''
        Takes an HTTP Request as parameter, and returns a HTTPRequest object
        containing the informations about the request 
        '''
        if not isinstance(request, bytes):
            request = request.encode(encoding)
        
        head = request.rsplit(b'\n')
        line = iter(head)
        rqline = next(line)

        rq = HTTPRequest(
            rqline.rsplit(b' ')[0].decode(encoding),
            rqline.rsplit(b' ')[1].rsplit(b'?')[0].decode(encoding),
            rqline.rsplit(b' ')[2].replace(b'\r', b'').decode(encoding)
        )
        
        if re.search(br'\?((\w*=\w*)&?)+', rqline.rsplit(b' ')[1]):
            for pair in re.findall(br'(\w*=\w*)', rqline.rsplit(b' ')[1]):
                param, arg = pair.replace(b'?', b'').replace(b'&', b'') \
                    .decode(encoding).split('=')
                rq.__params.append((param, arg))
        
        header = next(line)
        while header.replace(b'\r', b''):
            rq.add_header(*header.decode(encoding).split(': '))
            header = next(line)
        
        rq.__body = b'\n'.join(line)
        
        return rq
    
    @property
    def http_method(self):
        return self.__method
    
    @property
    def path(self):
        return self.__path
    
    @property
    def body(self):
        return self.__body
    
    @property
    def headers(self):
        return self.__headers
    
    def add_header(self, title, value):
        self.__headers.append((title, value))
    
    def get_header(self, header_name):
        return self.__headers.get(header_name, None)
    
    def cookies(self):
        cookies = self.__headers.get('Cookie')
        if cookies:
            return dict([c.split('=') for c in cookies.split('; ')])
        return None
    
    def __str__(self):
        requestline = ' '.join([self.__method, self.__path, self.__version])
        headers = '\n'.join(
            header for header in (': '.join(x) for x in self.__headers())
        )
        return '\n'.join([requestline, headers])+'\n\n'+self.__body.decode()
    
    def __repr__(self):
        return "{}({}, {}, {}, {}, {}, {})".format(
            self.__class__.__name__,
            self.__method.__repr__(),
            self.__path.__repr__(),
            self.__version.__repr__(),
            self.__headers.__repr__(),
            self.__params.__repr__(),
            self.__body.__repr__()
        )