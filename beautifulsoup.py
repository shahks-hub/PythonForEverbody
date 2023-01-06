# assignment week 3 course 3
# Scraping Numbers from HTML using Beautiful Soup
# url to use :  http://py4e-data.dr-chuck.net/comments_1689320.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
sum = 0
tags = soup('span')
for tag in tags:
    count += 1
    x = tag.contents[0]
    y = int(x)
    sum = sum + y

print('Count', count)
print('Sum' , sum)












