# assignment week 3 course 3
# FOLLOWING LINKS ON PYTHON
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaLues from the anchor tags, scan for a tag that is in a particular position
# relative to the first name in the list, follow that link and repeat the process a number
# of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL')
count = int(input('Enter count '))
position = int(input('Enter position '))-1


for i in range(count):
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tag = soup('a')
   link = (tag[position].get('href', None))
   url = link
   print('Retrieving:',link)
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tag = soup('a')
   name = tag[position].contents[0]








# name = tags[pos].contents[0] #Taking only the content from the desired positioned string
# print(name) #Printing the name













