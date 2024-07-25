# fine-tuning String extraction
import re

file_dir = '/home/jesse/VS_Code_Projects/Self_Learning/Python/Dr_Chuck/23_test.txt'

tar_lst = list()

with open(file_dir, 'r') as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall('\S+@\S+', line) 
        # it looks for all non-whitespace characters on both sides of '@'
        for match in matches:
            tar_lst.append(match) # avoid 2d list.

print(tar_lst)

# you can also add more conditions
sender = list()
receiver = list()
rec_email_only = list()

with open(file_dir) as file:
    for line in file:
        line = line.rstrip()
        matches = re.findall(r'^From[:] (\S+@\S+)', line)
        # here there are 2 conditions,
        # 1) start with 'From' or maybe with a ': ' after 'From'
        # 2) if '@' in it, get all the consecutive chars on both sides of '@'.
        for match in matches:
            sender.append(match)
        
         # Find emails after 'To:' or 'CC:'
        matches = re.findall(r'^(To|CC)[:] (\S+@\S+)', line, re.IGNORECASE)
        for match in matches:
            receiver.append(match)
        
        # Use non-capturing group for (To|Cc) and capture only the email
        matches = re.findall(r'^(?:To|Cc): (\S+@\S+)', line, re.IGNORECASE)
        for match in matches:
            rec_email_only.append(match)

print('Sender:', sender)
print('Receiver:', receiver)
print('Recipient Emails Only:', rec_email_only)


