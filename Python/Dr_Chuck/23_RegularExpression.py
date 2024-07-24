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

file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/23_test.txt'

# Find lines containing 'The'
print("Lines with 'The':")
with open(file_dir, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        if re.search('The ', line):  # Matches 'The ' anywhere in the line
            # here we use 'The ' so that 'They', 'There' and etc. would not give us any false alert
            print(line)

# Find lines starting with 'The'
print("\nLines starting with 'The':")
with open(file_dir, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        if re.search('^The ', line):  # Matches lines starting with 'The '
            print(line)

# find this pattern: X...:...
print('\nfind this pattern: X...:..')
with open(file_dir, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        if re.search('^X.*:', line):
            print(line)

# find this pattern: 'X-'+None_white_character+':'
print('\nfind this pattern: X followed by none white char then :')
with open(file_dir, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        if re.search('^X-\S+:', line):
            print(line)







