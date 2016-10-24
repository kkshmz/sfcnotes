#"client" side, using TCP
# this client will simply send a message to the server

import socket
import sys

#define a socket, nothing happened as yet
#AF_INET=IPV4, SOCK_STREAM=TCP mode
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define server address and port to be used(nothing happened as yet)
#in this case its localhost as we are only using 1 machine as both client and server
server_address = ('localhost', 10001)

#replace 'localhost' with the real hostname when using different machine as the server
#server_address = ('zmac032.sfc.keio.ac.jp', 10001)

now = time.strftime("%c")

print >>sys.stderr, 'connecting to %s port %d'% server_address

#connect to the server, this is from the "client" side, i.e the "active" side
sock.connect(server_address)

try:
  message = 'reqtime'
  print >>sys.stderr, 'sending "%s"'% message
#sending message to server, note that there is no address specified here because client and server are already connected
#sendall is also blocking
  sock.sendall(message)

  amount_received = 0
#in this case we know the expected length (we were the one who sent the original message, hence the message sent back from the server will be of the same length)
  amount_expected = len(message)

  while amount_received < amount_expected:
#receive data, recv is also blocking, it waits until data has been received, 256 is buffer size-in this case it's < len(message)
    data = sock.recv(256)

    amount_received += len(data)
    print >>sys.stderr, 'received "%s"'% data
finally:
#client close the connection(finally will always get executed no matter what is the status of "try") to make sure its a "clean exit"
  print >>sys.stderr, 'closing socket'
  sock.close()
