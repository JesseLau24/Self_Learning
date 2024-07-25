# similar to 31's code. just a different page
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://news.ycombinator.com/item?id=40345596')
for line in fhand:
    print(line.decode().strip())
    