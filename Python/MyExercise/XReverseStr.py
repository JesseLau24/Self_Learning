'''
Input: "Hello World"
Output: "World Hello"
'''

input = input('Input: ')
list = input.split()

for i in range(1, len(list)//2 + 1):
    list[i-1], list[-i] = list[-i], list[i-1]

output = ' '.join(list)
print(output)
