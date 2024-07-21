# Slicing a String

s = 'Monty Python'

# You can print the letters with indec of 0, 1, 2, 3 with this:
print(s[0:4]) # notice that 4 is not included here

# and any letters next to each other
print(s[3:7]) # 3, 4, 5, 6

print(s[6:7]) # only 6

# Python doesn't give you error message when slicing Strings:
print(s[6:10000]) # NO ERROR!!!

# String Concatenation
a = 'Hello'
b = a + 'World'

print(b)

c = a + ' ' + b

print(c)

# String Comparision
word = input('Input a word:')

if word == 'banana':
    print('Alright, banana')
elif word < 'banana':
    print(f'Your word {word} comes before banana')
else:
    print(f'Your word {word} comes after banana')










