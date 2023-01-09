# EXTRACTING DATA FROM JSON
# http://py4e-data.dr-chuck.net/comments_1689323.json
# The program will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json

data = input('Enter location: ')

print('Retrieving', data)

url = urllib.request.urlopen(data)
x = url.read()
print('Retrieved', len(x), 'characters')
info = json.loads(x)

count = 0
sum = 0
for item in info["comments"]:
     x= int(item['count'])
     sum = sum + x
     count += 1


print('Count:', count)
print('Sum:',sum)





