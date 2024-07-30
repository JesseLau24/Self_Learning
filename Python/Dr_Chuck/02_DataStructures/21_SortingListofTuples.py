# .items() method in dictionary returns a list of tuples
dict_1 = {'a': 12, 'c': 21, 'b': 19, 'd': 6}
temp = dict_1.items()
# here is a list of tuples
print(temp)
# which is 'class dict.items'
print(type(temp))

# sort it by keys
temp = sorted(temp) # 'dict_items' object has no attribute 'sort'
# so you cannot use 'temp.sort()'
print(temp)

# this is pretty convenient, just with Python
# not with any other languages
for k, v in temp:
    print(f'{k}: {v}')

# sort by value, not key
dict_2 = {'a': 13, 'b': 150, 'c': 9, 'd': 232}

# create an empty list
temp_1 = list()

# append the tuple of key and values in reversed order
for k, v in dict_2.items():
    temp_1.append((v, k))

print('reversed but unsorted:',temp_1)

# sort it:
temp_1 = sorted(temp_1, reverse=True)
print('reversed and sorted:', temp_1)

# change back the order:
temp_2 = list()
for v, k in temp_1:
    temp_2.append((k, v))
print('back to dict order k: v',temp_2)

# convert back
dict_2 = dict(temp_2)
print('converted back to dict:',dict_2)



