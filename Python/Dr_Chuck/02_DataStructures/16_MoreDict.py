# Counting words in file with dict
file_dir = '/home/jesse/Projects/Self_Learning/Python/Dr_Chuck/02_DataStructures/11_test.txt'
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

# keys and values: 
print('\nkey is the name, value is the value of the key')
for key in freq:
    print(key, freq[key])

# retrieving lists of keys and values

# method 1
print('\n1. list(freq):', list(freq))

# method 2
print('\n2. freq.keys():', freq.keys())

# get values:
print('\nfreq.values():', freq.values())

# get list of 2 tuples
print('\nfreq.items():', freq.items())

# two iteration variables
for aaa, bbb in freq.items():
    print(f'{aaa} : {bbb}')

