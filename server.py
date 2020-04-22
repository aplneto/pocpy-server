#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5000))
s.listen(5)
c, a = s.accept()
print("Conexão estabelecida com " + str(a[0]))
cont = 0
while True:
    resp = c.recv(2**10)
    cont += 1
    print(resp)
    print("Informação recebida:", cont)