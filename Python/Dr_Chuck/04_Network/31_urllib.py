# urllib is a Python library that does all socket work for us
# and makes web pages look like a file

# Import the necessary modules from the urllib package
import urllib.request, urllib.parse, urllib.error

# Open a connection to the URL provided and treat it as a file-like object
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Iterate over each line in the file-like object
for line in fhand:
    # Decode the line from bytes to a string and strip any leading/trailing whitespace
    print(line.decode().strip())

# we can also do whatever we want as if it were a file

# count word frequency

# Open a connection to the URL provided and treat it as a file-like object
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) +1
print(count)

