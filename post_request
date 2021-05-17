import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = socket.gethostbyname( 'transfer.sh' )
s.connect(( ipaddr,80 ))

header = ( """
POST /index.php HTTP/1.1
Host: transfer.sh
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://google.com
Cookie: PHPSESSID=blub
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
""" )

contentLength = "Content-Length: " + str( len( data ) ) + "\n\n"
request = header + contentLength
s.send( request )
response = s.recv( 4096 )
s.close()
print request
print response + '\n'
sys.exit( 0 )
