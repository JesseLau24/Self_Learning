# tuples are like lists, only they use () instead of [] or {}
# they have elements which are indexed starting 0
tuple_1 = ('Tom', 'Jerry', 'Topsy', 'Spike', 'Tyke', 'Butch')
print(tuple_1[0], tuple_1[1])

# they have tuple methods too
tuple_2 = (1, 3, 5, 2, 4, 6, 10, 12, 14, 11, 13, 15)
print(max(tuple_2))

# ut tuples are 'IMMUTABLE'
# meaning you cannot change it, similar to a String
try:
    tuple_1[0] = 'Thomas'
except:
    print('Error, cannot modify tuples')

str = 'This is a string'

try:
    str[5] = 'S'
except:
    print('Error, cannot modify Strings either')

# things not to do with tuples

# sort()
try:
    tuple_1.sort()
except:
    print('Error, cannot sort() tuples')

# append()
try:
    tuple_1.append('Mammy Two Shoes')
except:
    print('Error, cannot append() new element to tuples')

# reverse()
try:
    tuple_1.reverse()
except:
    print('Error, cannot reverse() tuples')




