astr = 'Hello Bob'
# Here it trys to run the code
# If the code fails, instead of printing error message and stop the code
# variable 'istr' would be given a String value of 'Not int'
try:
    istr = int(astr)
except:
    istr = 'Not int'

print('First:', istr)

astr = '123'
# Here, nothing wrong, so istr is converted
try:
    istr = int(astr)
except:
    istr = -1

print('Second:', istr)

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    # this line below won't execute 
    # because astr can't be converted to int
    # the 'try' block would end here and move to the 'except' block
    # Variable 'istr' would be 'Not int'
    print('There')
except:
    istr = 'Not int'

print('Third:', istr)

