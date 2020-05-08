from http_request import HTTPRequest
import pathlib

CODE_MESSAGES = {
    200: 'OK',
    404: 'Not Found'
    }

class WebSite:
    dynamic_pages = {}
    def __init__(self, index_folder: str = pathlib.Path.cwd()):
        self.__directory_iterator = pathlib.Path(index_folder)
        if not (self.__directory_iterator.exists()):
            raise ValueError ("The page directory must be valid")
    
    def get_page(self, request: HTTPRequest):
        if request.path in WebSite.dynamic_pages:
            page_function = WebSite.dynamic_pages[request.path]
            response_body = page_function(request)
        else:
            response_body = self.__find_page_file(request.path)
        
        return self.write_response(response_body)
    
    def __find_page_file(self, path: str):
        page_path = self.__directory_iterator / path
        if not page_path.exists():
            return None
        elif (page_path.is_dir()):
            files = list(page_path.glob('index.*'))
            if not files:
                return directory_listing(page_path)
        else:
            return static_page(str(page_path))
    
    def write_response(self, file):
        pass
    
    class Page(object):
        '''
        This is the decorator to be applied to any function that handles a
        request for a specific page. For example, if you have a function to
        handle requests to the login page you should write it like this:
            @WebSite.Page('/login')
            def login_handler(request: HTTPRequest)
        '''
        def __init__(self, full_page_path: str):
            self.page = full_page_path
        
        def __call__(self, function):
            WebSite.dynamic_pages[self.page] = function
        
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
        <title>{title_var}</title>
    '''
    return open(file_name, 'r').read().format(**keywords).encode("utf-8")

def directory_listing(directory_path: str):
    '''
    This functions creates an interactive directory listing to be displayed as
    an HTML page. This function should be overriden if you do not plan for your
    server to list directories
    '''
    iterator = pathlib.Path(directory_path)
    directory_string = ''
    file_string = ''
    page = f'''<!DOCTYPE html>
    <head>
        <title>index of {iterator.name}
    </head>
    <body>
    </body>'''