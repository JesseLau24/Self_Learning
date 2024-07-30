import os

# Define the working directory
cw_dir = os.getcwd()  + '/Python/Dr_Chuck/02_DataStructures/'
file_name = input('Input file name: ')
file_path = cw_dir + file_name

# Initialize the dictionary to store word frequencies
word_freq = {}

try:
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into words
            words = line.split()
            for word in words:
                # Convert words to lowercase for case insensitivity
                word = word.lower()
                # Increment the word frequency count
                word_freq[word] = word_freq.get(word, 0) + 1

except FileNotFoundError:
    print(f'Error: The file "{file_path}" was not found.')
    exit()
except Exception as e:
    print(f'Error: An unexpected error occurred: {e}')
    exit()

# Find the most frequent word
most_freq_word = None
highest_count = 0

for word, count in word_freq.items():
    if most_freq_word is None or count > highest_count:
        most_freq_word = word
        highest_count = count

print('Most frequent word:', most_freq_word)
print('Frequency:', highest_count)

# Count the total number of words
total_word_count = sum(word_freq.values())
print('Total word count:', total_word_count)

# Count the number of unique words
unique_word_count = len(word_freq)
print('Unique words count:', unique_word_count)


