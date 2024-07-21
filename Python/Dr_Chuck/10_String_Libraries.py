# String Libraries

# upper() and lower()
greet = 'Hello Bob'
zap = greet.lower() # convert all letters to lower case
zip = greet.upper() # convert all letters to upper case

print(f'greet: {greet}\nzap: {zap}\nzip: {zip}')

# You can even modify on an actual String
print('Hello, World'.lower())

# find() function: 

# returns the index of the item you pass to the parameter
# and returns -1 if not found
fruit = 'banana'
pos = fruit.find('na')

print(pos)

aa = fruit.find('m')
print(aa)

# replace() function
greet = 'Hello Bob'
new_greet = greet.replace('Bob', 'Jane')

print('new_greet:', new_greet)

new_greet = new_greet.replace('o', 'X')
print('new_greet:', new_greet)

# Stripping Whitespace:
greet = '     Hello, Bob.     '
print(greet, 'see, whitespace on both sides')

# we use lstrip() to strip the whitespace on the left
new_greet = greet.lstrip()
print(new_greet, 'see, still white space on the right')

# we use rstrip() to strip the whitespace on the right
new_greet = new_greet.rstrip()
print(new_greet,'no more white space on the right')

# Prefixes

line = 'Please have a nice day'

# startwith() checks if the String starts with something
# returns a Bolean value of either True or False
isFlag = line.startswith('Please')
print(isFlag)

isFlag = line.startswith('please')
print(isFlag)

# Parsing and Extracting
data = "From stephen.marquard@uct.ac.zza Sat Jann 5 09:14:16 2008"
# Task is to find the host of Stephen's email
# which is 'uct.ac.zza'

# Step 1, find @
atpos = data.find('@')
print('index of @:', atpos)

# Step w, find the first space after @
sppos = data.find(' ', atpos) 
# here, second papameter tells python to look from where
print('fisrt space after @:', sppos)

host = data[atpos+1:sppos]
print('Host:', host)



