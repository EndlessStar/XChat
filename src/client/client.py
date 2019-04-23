#!/usr/bin/env python3

from socket import *

HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input("Hello World!")
	if not data:
		break

	tcpCliSock.send(bytes(data, 'utf-8'))
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break

	print(data.decode('utf-8'))

tcpCliSock.close()