# List Methods

list_methods = ['append', 'count', 'extend', 'index', 'insert',
                'pop', 'remove', 'researve', 'sort']

# make an empty list
stuff = list()

# append items to list
stuff.append(list_methods[0])
stuff.append(list_methods[1])
stuff.append('something 9s')

print(stuff)

# is something in a list?
isFlag = 'append' in stuff
print(isFlag)

isFlag = 'book' in stuff
print(isFlag)

isFlag = 'apple' not in stuff # if not in stuff, returns True
print(isFlag)

# Built-in Functions anf List
nums = [71, 23, 9, 17, 5, 13, 2, 26, 8, 19, 33]
print('len()',len(nums))
print('max()', max(nums))
print('min()', min(nums))
print('sum()', sum(nums))
print('sum(nums)/len(nums)=average', sum(nums)/len(nums))

# exercise: input numbers and calculate average
usr_input = list()

while True:
    n = input('>>>')
    if n.lower() == 'done':
        break
    else:
        usr_input.append(float(n))
    
aver = sum(usr_input)/len(usr_input)
print('average:', aver)

