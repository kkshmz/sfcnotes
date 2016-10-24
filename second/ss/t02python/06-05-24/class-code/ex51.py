import urllib2
response = urllib2.urlopen('http://www.mit.edu/')
print 'RESPONSE:', response
print 'URL :', response.geturl()
headers = response.info()
print 'DATE :', headers['date']
print 'HEADERS :'
print '---------'
print headers
data = response.read()
print 'LENGTH :', len(data)
print 'DATA :'
print '---------'
print data
response = urllib2.urlopen('http://www.mit.edu/')
for line in response:
 print line.rstrip()