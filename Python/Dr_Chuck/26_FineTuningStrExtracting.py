# fine-tuning String extraction
import re

file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/23_test.txt'

tar_lst = list()

with open(file_dir, 'r') as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall('\S+@\S+', line)
        if len(matches) != 0:
            for i in matches:
                tar_lst.append(i)

print(tar_lst)



