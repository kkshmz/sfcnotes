#"server" side, using UDP, not TCP!
# this socket server will simply send back messages received from the client

import socket
import sys

#define a socket, nothing happened as yet
#AF_INET=IPV4, SOCK_DGRAM=UDP mode, This is Datagram/UDP socket!!
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#its localhost because this "server" program runs on  this machine.
#port 10001 is arbitrary selected
server_address = ('0.0.0.0',10001)

#bind is used to reserve the port (10001) for socket use
sock.bind(server_address)

#server start "listening" note there is no connect and accept here

while True:
  print >>sys.stderr, 'waiting for a connection, well this is connectionless actually'
#recvfrom is  blocking, it waits until data has been received, 4096 is buffer size
#note there is an address info here, unlike TCP
  data, address = sock.recvfrom(4096)
  print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
  print >>sys.stderr, data

  if data:
#send it back to the client (echo),  using sendto, not sendall, because its UDP. sendto is also blocking
# note there is an address info here
    sent = sock.sendto(data, address)
    print >> sys.stderr, 'sent %s bytes back to %s'%(sent, address)


#note there is no "close" here as this is  connectionless