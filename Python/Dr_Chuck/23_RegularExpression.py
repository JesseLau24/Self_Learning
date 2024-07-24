# regular expression quick guide
# .: Matches any single character except newline.
# ^: Matches the start of a string.
# $: Matches the end of a string.
# *: Matches 0 or more of the preceding element.
# +: Matches 1 or more of the preceding element.
# ?: Matches 0 or 1 of the preceding element; also makes preceding quantifier non-greedy.
# {n}: Matches exactly n occurrences of the preceding element.
# {n,}: Matches n or more occurrences of the preceding element.
# {n,m}: Matches between n and m occurrences of the preceding element.
# [...]: Matches any one of the characters inside the brackets.
# [^...]: Matches any one character not in the brackets.
# |: Acts as an OR operator; matches the pattern on the left or right.
# (): Groups elements or captures matched text.
# \: Escapes a special character or denotes a special sequence.
# \d: Matches any digit (equivalent to [0-9]).
# \D: Matches any non-digit.
# \w: Matches any word character (equivalent to [a-zA-Z0-9_]).
# \W: Matches any non-word character.
# \s: Matches any whitespace character.
# \S: Matches any non-whitespace character.
import re

file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/18_MushroomRock.txt'
fhand = open(file_dir)

# find lines with 'The'
print("lines with 'The_':")
for line in fhand:
    line = line.rstrip()
    if re.search('The ', line): # same as 'find()' method
        print(line)

fhand.close()

# Reopen the file:
fhand = open(file_dir)

# find lines start with 'The'
print("lines start with 'The_':")
for line in fhand:import re

file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/18_MushroomRock.txt'
fhand = open(file_dir)

# find lines with 'The'
print("lines with 'The_':")
for line in fhand:
    line = line.rstrip()
    if re.search('The ', line): # same as 'find()' method
        print(line)

fhand.close()

# Reopen the file:
fhand = open(file_dir)

# find lines start with 'The'
print("lines start with 'The_':")
for line in fhand:
    line = line.rstrip()
    if re.search('^The ', line): # here we use 'The ' so we filtered out 'They', 'There' and etc.
        print(line)
    line = line.rstrip()
    if re.search('^The ', line):
        print(line)








