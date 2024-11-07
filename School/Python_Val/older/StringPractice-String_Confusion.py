'''
Strings - Class Tasks
String Confusion

The user enters a name.

The user name is returned in reverse and begins with 
a capital also some extra text is added including 
the first letter of the user name

Example:
Valdis -> Sidlav, what a mess is it not V?
'''
def str_confusion(s:str) -> str:
    first_char = s[0]
    r_s = ''
    s = s.lower()
    for char in s:
        r_s = char + r_s
    
    r_s = r_s.title()
    r_s = r_s + f', what a mess is it not {first_char}?'
    return r_s

s = 'Valdis'
print(str_confusion(s))