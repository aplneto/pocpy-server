import re

class HTTPRequest(object):
    URL = r"([a-zA-Z\.\+\-]+://)" \
    r"([a-zA-Z0-9_\-\+\.]+:[a-zA-Z0-9_\-\+\.]*@)?" \
    r"([a-zA-Z0-9\-]{1,63}\.?)+" \
    r"(:\d{1-5})?" \
    r"(/(\w*)?)*" \
    r"(\?(\w*=\w*&?)*)?"

    def __init__(self, method: str, path: str, version: str):
        self.__method = method
        self.__path = path
        self.__version = version
        self.__headers = dict()
        self.__params = []
        self.__body = None

    @staticmethod
    def examine_request(request: bytes, encoding = 'utf-8'):
        '''
        Takes an HTTP Request as parameter, and returns a dictionary containing
        the informations about the request, including a 
        '''
        head = request.rsplit(b'\n')
        line = iter(head)
        rqline = next(line)

        rq = HTTPRequest(
            rqline.rsplit(b' ')[0].decode(encoding),
            rqline.rsplit(b' ')[1].rsplit(b'?')[0].decode(encoding),
            rqline.rsplit(b' ')[2].decode(encoding)
        )
        
        if re.search(br'\?((\w*=\w*)&?)+', rqline.rsplit(b' ')[1]):
            for pair in re.findall(br'(\w*=\w*)', rqline.rsplit(b' ')[1]):
                param, arg = pair.replace(b'?', b'').replace(b'&', b'') \
                    .decode(encoding).split('=')
                rq.__params.append((param, arg))
        
        header = next(line)
        while header.replace(b'\r', b''):
            rq.__headers.__setitem__(*header.decode(encoding).split(': '))
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
    def query_string(self):
        return query_string
    
    @property
    def body(self):
        return self.__body
    
    @property
    def headers(self):
        return self.__headers
    
    def get_header(self, header_name):
        return self.__headers.get(header_name, None)