# For Loop is also called Definite Loop

for i in range(5, 0, -1):
    print(i)
    # will finish printing all ints un this range
    # before ending the loop

print('Blastoff!')

# Another Example:

friends = ['Tom', 'Jerry', 'Butch', 'Topsy']

for friend in friends:
    print(f'Happy New Year, {friend}!')

print('Done!')

# Exercise: find the largest number in a list

nums = [1, 23, -9, 15, 87, 91, 93, 21, 46, 55, 51, 91, 123]

largest = nums[0]

for i in nums:
    if i > largest:
        largest = i
    print('largest so far:',largest)

print('Final result:', largest)

# Summing in a Loop
zork = 0
print('Before:', zork)

for i in nums:
    zork += i
    print('Sum:', zork, 'i:', i)

print('Finished. Total sum:', zork)

