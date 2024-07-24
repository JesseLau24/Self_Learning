# open file
file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/18_MushroomRock.txt'
fhand = open(file_dir)

# create an empty dict
words_freq = dict()

# count and store freq info into dict
for line in fhand:
    line = line.rstrip() # avoid counting whitespaces as words
    words = line.split()
    for word in words:
        words_freq[word] = words_freq.get(word, 0) + 1

# empty list for sorting
wds_freq_lst = list()

# append tuples to list in reversed order
for k, v in words_freq.items():
    wds_freq_lst.append((v, k))

# sort list of tuples form large to small
wds_freq_lst = sorted(wds_freq_lst, reverse=True)

# print top 10
print(wds_freq_lst[:10])

# store final result
top_ten = list()
for v, k in wds_freq_lst[:10]:
    top_ten.append((k, v))

print(top_ten)

# now we can iterate through them
for k, v in top_ten:
    print(f'top word: {k}\nfrequency: {v}\n')
