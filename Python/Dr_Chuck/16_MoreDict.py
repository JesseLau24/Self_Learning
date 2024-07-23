# Counting words in file with dict
file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/11_test.txt'
freq = dict()

try:
    with open(file_dir, 'r') as xfile:
        file_contents = xfile.readlines() # don't use '.read()'
        for line in file_contents:
            words = line.split()
            for word in words:
                freq[word] = freq.get(word, 0) + 1
except FileNotFoundError:
    print('File not found')
except IOError:
    print('An error occurred while reading the file.')

print(freq)



