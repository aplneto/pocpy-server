from http_request import HTTPRequest

class WebPage:
    def __init__(self, name: str, is_index = False, **kwargs):
        self.name = name
        self.__children = []
    
    def get(self):
        '''
        returns the page when accessed by the get method
        '''
        raise NotImplemented

    def post(self):
        '''
        '''
        return self.get()
    
    def __getitem__(self, request: HTTPRequest):
        path = request.path.split('/')
        response = self.find_page(path)
        if not response:
            return self.not_found()
        return response
    
    def find_page(self, path: list):
        if (path[0] == "" or path[0] == self.name):
            for page in self.__children:
                if page.name == path[1]:
                    return page.find_page[1:]
        return None
        
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