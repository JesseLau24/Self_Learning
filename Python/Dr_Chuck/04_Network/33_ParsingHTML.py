# Import necessary modules
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Prompt user for a URL
url = input('Enter- ')
# For example, input: http://www.dr-chuck.com/page1.htm

# Open the URL and read the HTML content
html = urllib.request.urlopen(url).read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags from the parsed HTML
tags = soup('a')

# Iterate over the list of anchor tags
for tag in tags:
    # Print the value of the href attribute, or None if the attribute is not present
    print(tag.get('href', None))



