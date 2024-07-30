# the regex version of finding host (instead od double spliting)
import re

lin = 'From: jessepinkman@gmail.com ETC 09:23:35 New Mexico'

y = re.findall('@([^ ]*)', lin) # Pattern @([^ ]*): This matches @ followed by zero or more non-space characters.
print(y)

# now we try to achieve this with files and also make it even cooler
file_dir = '/home/jesse/Projects/Self_Learning/Python/Dr_Chuck/03_RegularExpression/23_test.txt'

tar_lst = list()

with open(file_dir, 'r') as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall('^(from|to|cc)[:] .*@([^ ]*)', line, re.IGNORECASE)
        for match in matches:
            tar_lst.append(match)

print(tar_lst)



