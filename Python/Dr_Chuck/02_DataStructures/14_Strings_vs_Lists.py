# split() splits a String by whitespaces and returns a list
abc = 'with\nthree           words' 
# split() treats 'a lot of spaces' as 1
stuff =abc.split()

print(stuff)
print(stuff[-1]) # index -1 means the last item in a list

# but split() only works with spaces
line = 'one;two;three'
stuff = line.split()

print(stuff)

# but you can pass ';' as parameter to split by ';'
stuff = line.split(';')
print(stuff)

# get the email address
data = 'From: stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

data_list = data.split()

for i in data_list:
    if '@' in i:
        email = i

print(email)

# double split: get just the host
data = 'From: stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

data_list = data.split()

for i in data_list:
    if '@' in i:
        email = i
        host = email.split('@')[1]
        print('host:', host)









