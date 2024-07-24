# greedy matching: it always try to reach 
# the maxium length of the string
import re

x = 'From: Jesse to: Grace'
y = re.findall('^F.+:', x)
# instead of 'From:', it goes for 'From: Jesse To:'
# everytime it has the chance, it goes for the longest
print(y)

# non-greedy matching: just add a ?
z = re.findall('^F.+?:', x)
print(z)

