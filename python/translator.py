import sys


alphabet = list('abcdefghijklmnopqrstuvwxyz')
numbers = list('1234567890')

braille_alphabet = [
    'O.....',   # a
    'O.O...',   # b
    'OO....',   # c
    'OO.O..',   # d
    'O..O..',   # e
    'OOO...',   # f
    'OOOO..',   # g
    'O.OO..',   # h
    '.OO...',   # i
    '.OOO..',   # j
    'O...O.',   # k
    'O.O.O.',   # l
    'OO..O.',   # m
    'OO.OO.',   # n
    'O..OO.',   # o
    'OOO.O.',   # p
    'OOOOO.',   # q
    'O.OOO.',   # r
    '.OO.O.',   # s
    '.OOOO.',   # t
    'O...OO',   # u
    'O.O.OO',   # v
    '.OOO.O',   # w
    'OO..OO',   # x
    'OO.OOO',   # y
    'O..OOO'    # z
]

braille_numbers = [
    'O.....',   # 1
    'O.O...',   # 2
    'OO....',   # 3
    'OO.O..',   # 4
    'O..O..',   # 5
    'OOO...',   # 6
    'OOOO..',   # 7
    'O.OO..',   # 8
    '.OO...',   # 9
    '.OOO..'    # 0
]

# Checks if text is braille
def is_braille(text):
    # Check each character in text
    for c in text:
        if not(c in {'O','.'}):
            return False
    
    # Check length of text
    if not(len(text) % 6):
        return True
    
    return False

def braille_to_text(braille):
    # Make braille to alphabet lookup table
    alphabet_table = dict(zip(braille_alphabet,alphabet))

    # Add space character to table
    alphabet_table['......'] = ' '

    # Make braille to numbers lookup table
    numbers_table = dict(zip(braille_numbers,numbers))

    # Add decimal to numbers table
    numbers_table['..OO.O'] = '.'

    # Translate braille to text
    n = len(braille)
    cap_flag = False
    num_flag = False
    output_text = []
    for i in range(0,n,6):
        # Braille character
        b = braille[i:i+6]

        # Check if the following character is a capital
        if (b == '.....O'):
            cap_flag = True
            continue

        # Check if the following character is a decimal
        if (b == '.O...O'):
            num_flag = True
            continue
        
        # Check if the following character is a number
        if (b == '.O.OOO'):
            num_flag = True
            continue
        
        if (cap_flag):
            output_text.append(alphabet_table[b].capitalize())
            cap_flag = False
            num_flag = False
        elif (num_flag):
            output_text.append(numbers_table[b])
        else:
            output_text.append(alphabet_table[b])
            num_flag = False
    
    return ''.join(output_text)

def text_to_braille(text):
    # Make braille lookup table
    lookup_table = dict(zip(alphabet,braille_alphabet))

    # Add numbers to table
    lookup_table.update(zip(numbers,braille_numbers))

    # Add period to table
    lookup_table['.'] = '..OO.O'

    # Translate text to braille
    output_braille = []
    num_flag = False
    deci_flag = False
    for c in text:
        # Check if c is a space
        if (c == ' '):
            output_braille.append('......')
            num_flag = False
            deci_flag = False
            continue

        # Check if c is a number
        if c.isnumeric():
            # Check if c is the first number
            if not(num_flag):
                output_braille.append('.O.OOO')
                num_flag = True
            
            # Check if the last character is a decimal
            if deci_flag:
                # Remove period and add decimal
                deci = output_braille.pop()
                output_braille.append('.O...O')
                output_braille.append(deci)
                deci_flag = False

        # Check if c is (possibly) a decimal
        elif (c == '.' and num_flag):
            deci_flag = True
        
        else:
            num_flag = False
        
        # Check if c is uppercase
        if c.isupper():
            output_braille.append('.....O')
        
        output_braille.append(lookup_table[c.lower()])

    # Print translation
    return ''.join(output_braille)

# Translate and print commandline arguments
args = ' '.join(sys.argv[1:])
if is_braille(args):
    print(braille_to_text(args))
else:
    print(text_to_braille(args))