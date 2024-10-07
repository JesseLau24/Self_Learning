'''
3. Write a program for text conversion

Save user input

Prints the entered text without changes

Exception: if the words in the input are not .... bad, 
then the output is not ... the bad section must be changed to is good

The weather is not bad -> The weather is good

Car is not new -> Car is not new

This cottage cheese is not so bad -> This cottage cheese is good

Find (or index, or even rfind) will probably come in handy, as may an in operator. 
Also slice syntax will be useful.
'''
def text_converrer(s:str) -> str:
    not_index = s.find('not')
    bad_index = s.rfind('bad')
    if not_index == -1 or bad_index == -1 or not_index > bad_index:
        return s
    else:
        return s[:not_index] + 'good ' + s[bad_index + 3:]

str_test = input('Input string: ')
print(text_converrer(str_test))