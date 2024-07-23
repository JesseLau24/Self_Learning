import os

# the cwd is not this folder
cw_dir = os.getcwd()  + '/Python/Dr_Chuck/'
file_name = input('input file name: ')
file_dir = cw_dir + file_name

# create an empty dict
freq = dict()

# open file
try:
    fhand = open(file_dir)
    # create list of words
    for line in fhand:
        words = line.split()
        # create dict and count key values(frequency)
        for word in words:
            freq[word] = freq.get(word, 0) + 1
except:
    print('Error, check file name or directory.')

# variables that store the results
most_freq_key = None
count = 0

# freq.items() allows use of 2 iteration variables, which makes it simplier
for key, value in freq.items():
    if most_freq_key is None or value > count:
        most_freq_key = key
        count = value

# print results
print(most_freq_key, count)
