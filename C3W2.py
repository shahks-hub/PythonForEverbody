# assignment week 2 course 3


# The basic outline of this problem is to read the file, look
# for integers using the re.findall(), looking for a regular expression of
# '[0-9]+' and then converting the extracted strings to integers and summing
# up the integers.


import re

lst = list()

# reading the file and finding all integers
handle = open('real.txt')
for line in handle:
    x = re.findall('[0-9]+', line)
    for i in range(len(x)):
        num = int(x[i])
        lst.append(num)
print(sum(lst))









