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