# Understanding String

fruit = 'banana'

# the first leter 'b' has an index number of 0, then 1, 2, and etc.
print(f'First letter, fruit[0] is {fruit[0]}')
print(f'Second letter, fruit[1] is {fruit[1]}')

# Index is an operater, you can add () syntax and do math
x= 3
w = fruit[x-1]
print(w)

# You cna also get the length of a String with len() function
fruit_len = len(fruit)
print(f'Length of fruit is {fruit_len}')

# You can loop through Strings
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

print('Finish!')

# or like this:
index = 0

for i in fruit:
    print(index, i)
    index += 1

print('Finish!')

# count how many 'a's are there
count = 0

for i in fruit:
    if i == 'a':
        count += 1
    else:
        continue

print(f'The total number of letter a is {count}')


