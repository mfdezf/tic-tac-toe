import os

#model

keyboard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


#view

def print_keyboard(keyboard):
    '''To print Tic Tac Toe keyboard'''
    os.system('cls')

    print('Tic Tac Toe game\n')
    
    for r in range(0,3):
        for c in range(0,3):
            print(f'|{keyboard[r][c]}| ',end='')

        print('\n')

        if (r != 2):
            print('-----------\n')


def gather_plyr_pos():
    '''To gather the player's position'''

    pos = input('Please enter position: ')
    return int(pos)

#controler

def pos_validator(pos):
    '''To validate if user's input is in range 1 - 9'''

    if pos > 0 and pos < 10:
        return True

    else:
        return False

print_keyboard(keyboard)

pos_validator()





