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

#controler

print_keyboard(keyboard)




