import os

#model

keyboard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


#view

def print_keyboard(keyboard):
    '''To print Tic Tac Toe keyboard'''
    os.system('clear')

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

cont = 0        # Counter used to switch from X to O
while True:     # To make sure the user is entering valid values
      
    player = '' # To designate the player X or 0

    print_keyboard(keyboard)

    cont = cont + 1   # To switch from O to X

    if cont % 2 == 0:
        player = 'X'

    else:
        player = 'O'

    print(f'Player {player} turn')          # Print the name and gather the position
    ply_pos = gather_plyr_pos()

    if pos_validator(ply_pos):  
        continue
    
    else:
        cont = cont - 1                     # To keep current user if an invalid position was entered

    




