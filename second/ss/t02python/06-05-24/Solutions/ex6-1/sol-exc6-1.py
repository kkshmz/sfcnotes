fo = open("scrape.html", "r")
data = fo.read();
fo.close()

fo = open("log.txt", "w")
hey="This is a log file"
fo.write(hey)
fo.close()

