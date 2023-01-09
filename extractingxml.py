# EXTRACTING DATA FROM XML
# The program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts
# from the XML data, compute the sum of the numbers in the file.

#   http://py4e-data.dr-chuck.net/comments_42.xml
# sum= 2553
# counts = tree.findall('.//count')

# FORMAT OF THE DATA :
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = input('Enter location: ')
print('Retrieving', data)

url = urllib.request.urlopen(data, context=ctx)
x = url.read().decode()
print('Retrieved', len(x), 'characters')
tree = ET.fromstring(x)
counts = tree.findall('.//count')

count = 0
sum = 0
for item in counts:
     x= item.text
     count += 1
     sum = sum + int(x)

print('Count:', count)
print('Sum:',sum)





