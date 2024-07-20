# While Loop:

# Iteration Variable: it changes each times through a loop
n = 5

# Loop Body: keep looping until the condition is no longer true
while n > 0:
    print(n)
    n -= 1

# Only after the loop ends will the code after it starts running
print('Blastoff!')

# and now we see n is 0 instead of 5
print(n)

# Breaking Out of a Loop:

# most common way is to use 'break'
while True:
    line = input('> ')
    if line == 'exit':
        break
    # if the loop breaks, it jumps right out of the loop.
    # the line after 'break' in the loop body will Not be executed
    # no matter how many lines are there
    print(line)

print('Exited the program successfully!')

# continue will skip the lines after it and restart the loop
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    # ignor the folowing lines and restart the loop
    if line == 'exit':
        break
    print(line)

print('Exited the program successfully!')
