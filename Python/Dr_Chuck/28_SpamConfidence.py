import re

# Specify the file path to open
file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/28_mbox-short.txt'

# Open the file for reading
hand = open(file_dir)

# Create an empty list to store the numbers found
numlist = list()

# Iterate over each line in the file
for line in hand:
    # Remove any trailing whitespace from the line (including newline characters)
    line = line.rstrip()
    
    # Use regular expression to find patterns that match 'X-DSPAM-Confidence: [number]'
    # The pattern '^[X-DSPAM-Confidence: ([0-9.]+)' matches lines that start with
    # 'X-DSPAM-Confidence: ' followed by one or more digits or periods.
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    
    # If the pattern was not found exactly once, skip to the next line
    if len(stuff) != 1:
        continue
    
    # Convert the found string to a float
    num = float(stuff[0])
    
    # Append the float number to the list
    numlist.append(num)

# After processing all lines, find and print the maximum number from the list
print('Maximum:', max(numlist))











