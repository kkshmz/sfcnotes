import re
import urllib2

response = urllib2.urlopen('http://www.sfc.wide.ad.jp/IRL/contactus.html')

data = response.read()

match = re.findall(r'[\w.-]+@[\w.-]+',data)
#match = re.findall(r'0\d*-\d*-\d*',data)
#match = re.search(r'0\d*-\d*-\d*',data)

fo = open("log.txt", "w")
if match:
   fo.write('\n'.join(match))

fo.close()

