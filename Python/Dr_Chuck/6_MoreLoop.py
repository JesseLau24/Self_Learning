# Finding the Average
nums = [1, 22, 13.4, 22, 15, 23, 12, -9, 22, -17, 33.75, 22, -22, 120, 34]

count = 0
sum = 0

for i in nums:
    sum += i
    count += 1
    average = sum / count
    print(f'Iteration {count}, running sum: {sum} running average: {average}')

print('Finished. Average:', average)

# Filtering in Loop for numbers greater than 20
print('Numbers > 20:')

for i in nums:
    if i > 20:
        print(i)
    else:
        continue
    # else part is not necessary

print('Finished')

# Check if 22 is in the list, and if so how many
found = False
count = 0

for i in nums:
    if i == 22:
        found = True
        count += 1
        print(f'Found {count} 22')

print(f'Finished. Found {count} 22')

# Check if all items are > 13, and count how many for each
count_small = 0
count_larger = 0

for i in nums:
    if i == 13:
        continue # to skip == 13
    elif i > 13:
        print(i, "> 13")
        count_larger += 1
    else:
        print(i, '< 13')
        count_small += 1

print(f'Finish. {count_larger} items larger than 13, {count_small} smaller.')

# Find the Smallest
smallest = None # here we can use None

for i in nums:
    if smallest is None: # is operator checks both value and type
        smallest = i
    elif i < smallest:
        smallest = i
        print('Current Smallest:', smallest)

print('Finish. smallest:', smallest)







