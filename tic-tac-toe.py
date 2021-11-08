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
        input('Incorrect position, the value entered must in the range (0 - 9), press any key to continue')
        return False

while True:     #To make sure I'm gathering correct data

    print_keyboard(keyboard)

    ply_pos = gather_plyr_pos()

    if pos_validator(ply_pos):
        break

    




