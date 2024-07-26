import urllib.request, urllib.parse, urllib.error  # Import the urllib library for opening and reading URLs
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import ssl  # Import the ssl library to handle SSL certificate issues

# Ignore SSL certificate errors
ctx = ssl.create_default_context()  # Create a default SSL context
ctx.check_hostname = False  # Disable hostname verification (ignore SSL certificate hostname check)
ctx.verify_mode = ssl.CERT_NONE  # Disable certificate verification (ignore SSL certificate validation)

url = input('Enter - ')  # Prompt the user to enter a URL (e.g., http://www.dr-chuck.com/)
html = urllib.request.urlopen(url, context=ctx).read()  # Open the URL, apply SSL context to ignore certificate errors, and read the HTML content
soup = BeautifulSoup(html, 'html.parser')  # Parse the HTML content using BeautifulSoup with the 'html.parser' parser

# Retrieve all of the anchor tags
tags = soup('a')  # Find all <a> (anchor) tags in the HTML content
for tag in tags:  # Iterate over each <a> tag
    print(tag.get('href', None))  # Print the value of the 'href' attribute of each <a> tag; if the 'href' attribute is missing, print 'None'





