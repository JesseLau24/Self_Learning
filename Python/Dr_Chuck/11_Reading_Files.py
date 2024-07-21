import os
# Reading Files with open() function

# open() function creates a handle
# to make it possible for us to read and write the file
try:
    fhand = open('mbox.txt')
    print(fhand)
except:
    print('No such file or directory')

# the Newline Character \n to indicate when a line ends
stuff = 'Hello, world!\nNow it goes to the next line!'
print(stuff)

# \n takes 1 character
stuff = 'X\nY'
print(stuff)
print('len(stuff):', len(stuff))

# here is to open the 11_test.txt

# when open files, recommend to use try block
try:
    with open('11_test.txt', 'r') as file:
        file_contents = file.read()
    print(file_contents)
except FileNotFoundError:
    print('File not found')
except IOError:
    print('An error occurred while reading the file.')

# it fails because current directory is:
print('current working directory:',os.getcwd())

# now we need the correct directory of the test file
file_dir = '/home/jesse/VS_Code_Project/Self_Learning/Python/Dr_Chuck/11_test.txt'
try:
    with open(file_dir, 'r') as xfile:
        file_contents = xfile.read()
    print('\nFile Contents:')
    print(file_contents)
    print('Len(file_contents):', len(file_contents))
    # here, we consider file_contents as a long String with '\n'
except FileNotFoundError:
    print('File not found')
except IOError:
    print('An error occurred while reading the file.')

# but if the file has too many lines,
# not advisable to read it like this

# Counting lines in a file
fhand = open(file_dir, 'r')
print('This is how a handle looks like:\n', fhand)
count = 0
for lines in fhand:
    count += 1
print('Lines count:', count)


