#"server" side, using UDP, not TCP!
# this client will simply send a message to the server

import socket
import sys

#define a socket, nothing happened as yet
#AF_INET=IPV4, SOCK_DGRAM=UDP mode, This is Datagram/UDP socket!!
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#define server address and port to be used(nothing happened as yet)
#in this case its localhost as we are only using 1 machine as both client and server
#server_address = ('localhost', 10001)

#replace 'localhost' with the real hostname when using different machine as the server
server_address = ('avdamac01.sfc.keio.ac.jp', 10001)

message = 'This is the message. It will be repeated.'
print >>sys.stderr, '(sort of) connecting to %s port %d'% server_address

try:
  print >>sys.stderr, 'sending "%s"'% message
  
#send  message to the server using sendto, not sendall, because its UDP. sendto is also blocking
#note there is an address info here, unlike TCP
  sent = sock.sendto(message, server_address)

  print >>sys.stderr, 'waiting to receive'

#recvfrom is  blocking, it waits until data has been received, 4096 is buffer size
#note there is an address info here, unlike TCP
  data, server = sock.recvfrom(4096)
  print >>sys.stderr, 'received "%s"', data

finally:
#it's the client that close the connection(finally will always get executed no matter what is the status of "try") to make sure its a "clean exit"
  print >>sys.stderr, 'closing socket'
  sock.close()
