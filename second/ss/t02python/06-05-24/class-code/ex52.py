"""
first step to improving your HTTP web services client is to identify yourself properly with a User-Agent. To do that, you need to move beyond the basic urllib and dive into urllib2.
"""
import urllib2
request = urllib2.Request('http://www.mit.edu/')
request.add_header('User-agent', 'SFC (http://www.sfc.keio.ac.jp/)')
# unfortunately we can not see our header except looking directly on MIT's web server.
response = urllib2.urlopen(request)
headers = response.info()
print headers
data = response.read()
print data