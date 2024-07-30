# using the code in RegularExpression.py as an example
import re

file_dir = '/home/jesse/Projects/Self_Learning/Python/Dr_Chuck/03_RegularExpression/23_test.txt'

# Find lines containing 'The'
print("Lines with 'The':")
with open(file_dir, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        print(f"Processing line: {line}", flush=True)  # Debugging: Print each line before processing
        if re.search('The ', line):  # Matches 'The ' anywhere in the line
            print(f"Matched line: {line}", flush=True)  # Debugging: Print matched line

# Find lines starting with 'The'
print("Lines starting with 'The':")
with open(file_dir, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        print(f"Processing line: {line}", flush=True)  # Debugging: Print each line before processing
        if re.search('^The ', line):  # Matches lines starting with 'The '
            print(f"Matched line: {line}", flush=True)  # Debugging: Print matched line


