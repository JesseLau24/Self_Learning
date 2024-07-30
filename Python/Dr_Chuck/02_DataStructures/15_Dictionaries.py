# list vs dictionary:
# list is a collection of values in order
# a dictionary is a bag of values that has labels

# creat an empty dictionary:
pack = dict()

# put things in it
pack['money'] = 1200
pack['water'] = 3
pack['cat'] = 4
pack['cyber deck'] = 1
pack['battery'] = 6
pack['gun'] = 0

print(pack)

# update dictionary:
pack['money'] += 2000

# now you see 'money' is 3200:
print(pack)
print(pack['money'])

# make a full dictionary
character = {'Alestair': 1, 'Morrigan': 1, 'Zevran': 0, 'Liliana': 1}
print(character)

# Exercise: count frequency
letters = ['a', 'b', 'c', 'a', 'c', 'd', 'a', 'd', 'a', 'b', 'c', 
         'a', 'c', 'd','a', 'c', 'd', 'a', 'd', 'a', 'd', 'a', 'b']

freq = dict()

for i in letters:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)

# get() method
freq_a = freq.get('a', 0)
# it checks if 'a' exist in dict freq
# if exits, returns the frequency, else, returns 0
print('a', freq_a)

freq_e = freq.get('e', 0)
print('e', freq_e)

# so the previous exercise could be rewritten:
letters = ['a', 'b', 'c', 'a', 'c', 'd', 'a', 'd', 'a', 'b', 'c', 
         'a', 'c', 'd','a', 'c', 'd', 'a', 'd', 'a', 'd', 'a', 'b']

freq = dict()

for i in letters:
    freq[i] = freq.get(i, 0) + 1

print(freq)





