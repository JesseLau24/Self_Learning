# Algorithms: a set of rules or steps used to solve a problem
# Data structures: a paeticular way of organizing data in a computer

# A list is a lind of Collection
friends = ['Joe', 'Glenn', 'Sally']
carryon = ['apple', 'shirt', 'perfume']

# you can print the whole list
print(friends)

# or you can loop through a list:
for i in friends:
    print('Name:', i)

# and this:
if len(friends) == len(carryon):
    for i in range(0, len(friends)):
        print(f'{friends[i]}: {carryon[i]}')

# adding list together
together = friends + carryon
print('added together:',together)

# 2 dimensional list: a list with items being list
list2d = [friends, carryon]
print('2D list:', list2d)

# modify list
list2d[0][2] = 'Mandy'
print('Modified:',list2d)

# slacing list:
print('slacing together[1:4]:',together[1:4])
print('slacing together[:4]:',together[:4])
print('slacing together[3:]:',together[3:])




