import os

# the cwd is not this folder
cw_dir = os.getcwd()  + '/Python/Dr_Chuck/'
file_name = input('input file name: ')
file_dir = cw_dir + file_name

freq = dict()

try:
    fhand = open(file_dir)
    for line in fhand:
        words = line.split()
        for word in words:
            freq[word] = freq.get(word, 0) + 1
except:
    print('Error')

# count most frequent word:
most_freq_word = None
count = 0

for key, value in freq.items():
    if most_freq_word is None or value > count:
        most_freq_word = key
        count = value

print('most frequent word:', most_freq_word, '\nfrequency:', count)

# count overall word count:
sum = 0

for key in freq:
    sum += freq[key]

print('total word count:', sum)



