#!/usr/bin/python
# Open a file
fo = open("log.txt", "r")
str = fo.read();
print "Read from file: ", str
# Close opend file
fo.close()
