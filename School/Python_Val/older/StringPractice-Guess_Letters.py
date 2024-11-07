'''
2. Write a program to recognize a text symbol

The user (first player) enters the text.

Only asterisks are output instead of letters. Suppose there are no numbers, 
but there may be spaces

The user (i.e. the other player) enters the symbol.

If the letter is found in the string, then the letter is displayed in the 
appropriate places, all other letters remain asterisks.

Potato field -> ****** *****

User enters o -> *o***o *****

In principle, this is a good start for the game of hangman (possible final project).
'''

def convert_asterisks(s:str) -> str:
    asterisks = ''

    for char in s:
        if char != ' ':
            asterisks += '*'
        else:
            asterisks += char

    return asterisks

def reveal_letters(s:str, c:str) ->str:
    r_s = ''
    for item in s:
        if c == item:
            r_s += c
        else:
            r_s += '*'

    return r_s

def merge_strings(a, b):
    if len(a) != len(b):
        raise ValueError("Strings must be of equal length.")
    
    merged = []
    for char_a, char_b in zip(a, b):
        if char_a == '*' and char_b == '*':
            merged.append('*')
        elif char_a == '*':
            merged.append(char_b)  
        elif char_b == '*':
            merged.append(char_a)  
        else:
            merged.append(char_b) 
    
    return ''.join(merged)

# Game Body:
words = input('Player 1 inputs words: ')
print(convert_asterisks(words))

game_over = False
revealed = convert_asterisks(words)
while not game_over:
    c = input('Player 2 input letter: ')
    temp = reveal_letters(words, c)
    revealed = merge_strings(temp, revealed)
    print(revealed)
    
    if revealed == words:
        game_over = True
        print('Game Finished! You have guessed the word!')
    





