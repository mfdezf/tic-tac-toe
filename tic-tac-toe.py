import os

#model

keyboard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def insert_mark(ply_pos, player):
    '''To insert a mark in the keyboard'''
    
    if ply_pos == 7:
        keyboard[0][0] = player
    
    elif ply_pos == 8:
        keyboard[0][1] = player

    elif ply_pos == 9:
        keyboard[0][2] = player
    
    elif ply_pos == 4:
        keyboard[1][0] = player
    
    elif ply_pos == 5:
        keyboard[1][1] = player

    elif ply_pos == 6:
        keyboard[1][2] = player
    
    elif ply_pos == 1:
        keyboard[2][0] = player
    
    elif ply_pos == 2:
        keyboard[2][1] = player

    elif ply_pos == 3:
        keyboard[2][2] = player

def mark_insertion_checker(ply_pos):
    '''To determine if the position in the keyboard is empty so can be marked'''
    
    if ply_pos == 7 and keyboard[0][0] == ' ':
        return True
        
    elif ply_pos == 8 and keyboard[0][1] == ' ':
        return True

    elif ply_pos == 9 and keyboard[0][2] == ' ':
        return True
    
    elif ply_pos == 4 and keyboard[1][0] == ' ':
        return True
    
    elif ply_pos == 5 and keyboard[1][1] == ' ':
        return True

    elif ply_pos == 6 and keyboard[1][2] == ' ':
        return True
    
    elif ply_pos == 1 and keyboard[2][0] == ' ':
        return True
    
    elif ply_pos == 2 and keyboard[2][1] == ' ':
        return True

    elif ply_pos == 3 and keyboard[2][2] == ' ':
        return True

    else: 
        input('The position is not empty, press any key to retry')
        return False

def winner_tie_validator():
    '''To determine if there is a winner or a tie'''
    
    valindation_mark_row = None         #To compare for the number of ocurrences of a mark to determine a winner
    mark_counter_row = 0                #To count the times that a mark repeats

    # To check winners by row

    for r in range(0,3):
        for c in range(0,3):
            if c == 0 and keyboard[r][c] !=' ':
                valindation_mark_row = keyboard[r][c]
            
            if valindation_mark_row != None and valindation_mark_row == keyboard[r][c]:
                mark_counter_row += 1
                if mark_counter_row == 3:
                    return True
        
        valindation_mark_row = None
        mark_counter_row  = 0   # reset counter to check a new row

    
    # To check winners by column

    valindation_mark_column = None                # To compare for the number of ocurrences of a mark to determine a winner
    mark_counter_column = 0                       # To count the times that a mark repeats

    for r in range(0,3):
        for c in range(0,3):
            if c == 0 and keyboard[c][r] !=' ':
                valindation_mark_column = keyboard[c][r]
            
            if valindation_mark_column != None and valindation_mark_column == keyboard[c][r]:
                mark_counter_column += 1
                if mark_counter_column == 3:
                    return True
        
        valindation_mark_column = None
        mark_counter_column = 0   # reset counter to check a new column


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

    if pos_validator(ply_pos) and mark_insertion_checker(ply_pos):  
        insert_mark(ply_pos, player)
        print_keyboard(keyboard)
        
        if winner_tie_validator():
            print('We have a winner!!')
            break
        
    
    else:
        cont = cont - 1                     # To keep current user if an invalid position was entered

    




