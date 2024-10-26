# Get User input:
start = int(input('Start: '))
end = int(input('End: '))

# For Loop
for i in range(start, end+1):
    # Store the value message, later decide if it should come with ', '
    if i % 5 == 0 and i % 7 == 0:
        message = 'FizzBuzz'
    elif i % 5 == 0:
        message = 'Fizz'
    elif i % 7 == 0:
        message = 'Buzz'
    else:
        message = i
    # Decide if it is the last in the row.
    if i != end:
        print(message, end=', ')
    else:
        print(message, end=' \nxxxxxxxxxxxxxxxx\nFinished!\n') 
        