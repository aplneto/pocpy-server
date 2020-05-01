# URL Format: scheme://[user:password@]host:[port][/path][?parameter=argument]

import http_request

exmaple = b'POST /bla/bla.py HTTP/1.1\r\nhost: localhost:13600\r\nConnection: keep-alive\r\nContent-Length: 24\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nusername=adam&senha=adam'

d = http_request.HTTPRequest.examine_request(exmaple)
print(repr(d))