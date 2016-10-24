import re


fo = open("scrape.html", "r")
data = fo.read();
fo.close()

#match = re.findall(r'[\w.-]+@[\w.-]+',data)
#match = re.findall(r'0\d*-\d*-\d*',data)
match = re.search(r'0\d*-\d*-\d*',data)

fo = open("log.txt", "w")
if match:
   fo.write('\n'.join(match))

fo.close()

