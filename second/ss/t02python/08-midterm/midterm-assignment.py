#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2
from scipy import misc
import numpy as np
import mechanize
import re
import json
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(""http://www.formula1.com/content/fom-website/en/championship/results/2016-race-results/2016-australia-results/race.html"))
br = mechanize.Browser()
inital = open('list.json')

#PART 1
#Save(locally) the images and the html of the URLs specified inside <list.json>
#File names are <1.jpg>, <2.jpg>  for images and <1.html>, <2.html> so on.
#You’ll need to do your own research on how to use urllib module(or any other) to do this.
# Again your script should work for any number of URLs in <list.json>

initialread = json.loads(


#PART 2
#Access this URL(using python script) http://www.formula1.com/content/fom-website/en/championship/results/2016-race-results/2016-australia-results/race.html
#and extract points (last column) and family names of the drivers from the “table”.
#You can extract it to whatever data structure of your choice.
br.open("http://www.formula1.com/content/fom-website/en/championship/results/2016-race-results/2016-australia-results/race.html")
br.

#PART 3
#Prompt user “how many URL(s)  to be processed ?”
#user inputs a number
#Check and only accept input only if it’s numbers/numeric,
# Also check if the number is less than same to the number of URLs in <list.json>

url = raw_input('How many URL(s) to be processed? ')
   if url 'str(int)'
else if:

#PART 4
#If the URL is an image(not html): Rotate (90 degrees) the selected images
#save the result as output files named rotated_<ORIGINAL FILE NAME>.jpg

#read image file and conver it into 'img-x' which is a NumPy Array Format
img-1 = misc.imread('1.jpg')
img-2 = misc.imread('2.jpg')
img-3 = misc.imread('3.jpg')
img-4 = misc.imread('4.jpg')

#getting the images size into variables
lx, ly = img-1
lx, ly = img-2
lx, ly = img-3
lx, ly = img-4

#rotation of the images by 90 degrees
rotated-img-1 = ndimage.rotate(img-1, 90)
rotated-img-2 = ndimage.rotate(img-2, 90)
rotated-img-3 = ndimage.rotate(img-3, 90)
rotated-img-4 = ndimage.rotate(img-4, 90)

#saving the output
#rotated one is rotated-img-x
misc.imsave('rotated-img-1, img-1')
misc.imsave('rotated-img-2, img-2')
misc.imsave('rotated-img-3, img-3')
misc.imsave('rotated-img-4, img-4')

#PART 5

#URL of images
match-image = re.findall(r'http://+[\w]+.jpg', data)
print match-image

#URL of html
match-html = re.findall(r"http://+[\w]+.jpg', data)
print match-html

#family names

#points


#PART 6
## for printing the URL of the images and the html on the page.
f=open('filename')
lines=f.readlines()
## Assign line numbers of the images nad hte html here
print lines[25]
print lines[29]

#PART 7
#For opening a file named log.txt and adding information from #6
fo = open("log.txt", "w")
images = ""
fo.write()
fo.close()
