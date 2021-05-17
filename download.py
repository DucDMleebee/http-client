import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('transfer.sh', 80))
s.sendall(b'GET /image/png HTTP/1.1\r\nHOST: transfer.sh\r\n\r\n')

reply = b''

while select.select([s], [], [], 3)[0]:
    data = s.recv(2048)
    if not data: break
    reply += data

headers =  reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]

# save image
f = open('image.png', 'wb')
f.write(image)
f.close()
