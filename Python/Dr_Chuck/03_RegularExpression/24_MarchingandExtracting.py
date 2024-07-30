# matching and extracting

# re.search() returns a Boolean value if or not the String matches
# the regular expression (pattern)

# re.findall() returns a list that contains all the Strings that
# match the regular expression (pattern)

# example:
import re

x = 'My 2 favorite numbers are 199234 and 423715'

# here [0-9] means single digit int numbers
y = re.findall('[0-9]', x)
print(y)

# here [0-9]+ means int numbers, but can be multi digits
# if digits are consecutive
z = re.findall('[0-9]+', x)
print(z)

# another example:
file_dir = '/home/jesse/Projects/Self_Learning/Python/Dr_Chuck/03_RegularExpression/23_test.txt'

tar_lst = list()

with open(file_dir, 'r') as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall('^X-\S+:', line)
        tar_lst.extend(matches)  # Append matches to the list

print(tar_lst)

# we can also search all 'f' words
file_dir = '/home/jesse/Projects/Self_Learning/Python/Dr_Chuck/02_DataStructures/18_MushroomRock.txt'

f_words = set() # use set to automatically handle duplicate

with open(file_dir, 'r') as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall(r'\b[fF]\w*', line)
        f_words.update(matches)

# convert to list:
f_words = list(f_words)
print('f words in mushroom Rock:\n', f_words)

# or create dict to count frequency:
file_dir = '/home/jesse/Projects/Self_Learning/Python/Dr_Chuck/02_DataStructures/18_MushroomRock.txt'

f_words = dict()

with open(file_dir, 'r') as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall(r'\b[fF]\w*', line)
        for i in matches:
            f_words[i] = f_words.get(i, 0) +1

# then we sort it
temp = list()

for k, v in f_words.items():
    temp.append((v, k))

temp = sorted(temp, reverse=True)

f_word_sorted = dict()
for v, k in temp:
    f_word_sorted[k] = v

print('\nf_word_sorted:\n', f_word_sorted)
