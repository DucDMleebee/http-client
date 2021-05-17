#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("transfer.sh" , 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: transfer.sh\r\nAccept: text/html\r\nConnection: close\r\n\r\n")

    while True:

        data = s.recv(1024)

        if not data:
            break

        print(data.decode())
