#"server" side, using TCP
# this socket server will simply send back messages received from the client

import socket
import sys

#define a socket, nothing happened as yet
#AF_INET=IPV4, SOCK_STREAM=TCP mode
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#its localhost because this "server" program runs on  this machine.
#port 10001 is arbitrary selected, up to 1024 is previleged port
# 0.0.0.0 means its accepting connections from all hosts (typical case)
server_address = ('0.0.0.0',10001)

#bind is used to reserve the port (10001) for socket use
sock.bind(server_address)

#server start listening for connection
''''
1 specifies "backlog".The backlog argument specifies the maximum number of queued
#connections and should be at least 0; the maximum value is system-dependent (usually 5),
the minimum value is forced to 0
'''''
sock.listen(1)

while True:
  print >>sys.stderr, 'waiting for a connection'
#accept is blocking: it waits for connection before returning
#connection  is a new socket object usable to send and receive data on the connection
#address is the address bound to the socket on the other end of the connection
  connection, client_address = sock.accept()
  
#try-finally structure (similar to Java)

  try:
    print >>sys.stderr,'connection from', client_address
    while True:
#recv is also blocking, it waits until data has been received, 256 is buffer size
      data = connection.recv(256)
      print >>sys.stderr, 'received "%s"'%data
      if data:
        print >>sys.stderr, 'sending data back to the client'

#send it back to the client (echo), sendall is also blocking
        connection.sendall(data)
      else:
        print >>sys.stderr, 'no more data from', client_address
#if no more data received then quit try block       
        break
  finally:
#server close the connection(finally will always get executed no matter what is the status of "try") to make sure its a "clean exit"
    connection.close()

