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
