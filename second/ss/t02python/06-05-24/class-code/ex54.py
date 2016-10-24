import mechanize

br = mechanize.Browser()
br.open("http://www.google.com/")
print br.title()
print br.geturl()
print br.response().read()

