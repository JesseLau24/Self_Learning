'''
Create a program that builds a pyramid out of symbols.


 There should be a variable specifying height of pyramid. 

Bonus: ask user for the height! 

 Pyramid starts with 1 symbol (for example *) It keeps expanding to 3 symbols, 5 symbols, etc 

 60% of grade for HW1 will be given for pyramid making single symbols 

 80% of grade will be given if the symbols alternate (for example * and #)

# 100% of grade will be given for those whose pyramid is made from your first name letters (repeating) So for "VALDIS" 

      V 

     AAA 

    LLLLL 

   DDDDDDD 

  IIIIIIIII 

 SSSSSSSSSSS 

VVVVVVVVVVVVV


PS Your pyramid with your name symbols might not look too hot, if you have a regular font . For best results use monospace type font, but you will not be graded on your font choice.

PSS To make it slightly easier, maximum number of height will be 40.
'''
def star_pyramid(height: int) -> str:
    for i in range(1, height + 1):
        print(' ' * (height - i) + (2 * i -1) * '*')

def list_pyramid(list:list, height) -> str:
    for i in range(1, height + 1):
        print(' ' * (height - i) + (2 * i - 1) * list[(i - 1)%len(list)])

def name_pyramid(list: list) -> str:
    for i in range(1, len(list) + 1):
        print(' ' * (len(list) - i) + list[i-1] * (2 * i - 1))
choice = input('''
               Please select your choice:
               1 to print pyramid with symbols of your choice
               2 to print pyramid with your first name
               any other symbol to print pyramid of *
               ''')

if choice == '1':
    height = int(input('Input height of the pyraimd: '))
    list = list(input('Input the symbols you like(without space or comma inbetween): '))
    list_pyramid(list, height)
elif choice == '2':
    list = list(input('Your fisrt name: '))
    name_pyramid(list)
else:
    height = int(input('Input height of the pyraimd: '))
    star_pyramid(height)

