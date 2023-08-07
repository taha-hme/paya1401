import numpy as np
import os
from colorama import Fore
from time import sleep

def clear():
    #This function clears the command.
    if os.name == 'nt':
        _ = os.system('cls') #For Windows
    else:
        _ = os.system('clear') #For Mac or Linox
clear()

def Loading():
    a = 'Hi and welcome to this part.\nYou can read help with 1,'
    x = input(Fore.LIGHTYELLOW_EX + f'{a} pass the help with 2 and exit with 0: ')
    print(Fore.WHITE + '')
    match x:
        case '1':
            clear()
            HelpOfGame()
            Starting()
            PlayWithComputer()
        case '2':
            clear()
            Starting()
            PlayWithComputer()
        case _:
            clear()
            exit(0)

def Starting():
    GameNotes()
    TextToStart()

def PlayWithComputer():
    x1 = y1 = Num1 = 0
    z = []
    l = [v for v in range(9)]
    NewTable = np.append(z, table)
    lst = [0, 1]
    i = np.random.choice(lst, p=[0.5, 0.5])
    if i == 0:
        k = 0
        print(Fore.LIGHTGREEN_EX + f'{player1} starts the game.\n' + Fore.WHITE)
    elif i == 1:
        k = 1
        print(Fore.LIGHTGREEN_EX + f'{player2} (Bot) starts the game.\n' + Fore.WHITE)
    sleep(1)
    clear()
    while i < (9 + k):
        if Winner1() == True or Winner2() == True:
            break
        if i%2 == 0:
            print(Fore.WHITE + f'Table =\n{table}\n')
            n1 = int(input(Fore.YELLOW + f'Please enter a correct number {player1} {a}' + Fore.WHITE))
            x1, y1, Num1 = (n1 // 10) % 10, n1 % 10, 1
            if not(x1 > 2 or y1 > 2 or table[x1][y1] != 0):
                i += 1
                table[x1][y1] = Num1
                clear()
            else:
                print(f'Table =\n{table}\n')
                clear()
                continue
        else:
            print(Fore.WHITE + f'Table =\n{table}\n')
            In = np.random.choice(l)
            l.pop(l[In])
            for x in l:
                if x == In:
                    NewTable[l[x]] = 2
            for t in range(9):
                if NewTable[t] == 0 and l[x] == t:
                    ChangeValue(NewTable, table)
                    i += 1
                    clear()
                    break
                if NewTable[t] != 0 and l[x] == t:
                    In = np.random.choice(l)
                    continue
    if Winner1() == True:
        clear()
        print(Fore.CYAN + f'{player1} wins.' + Fore.WHITE)
    if Winner2() == True:
        clear()
        print(Fore.CYAN + f'{player2} (Bot) wins.' + Fore.WHITE)
    if Winner1() == False and Winner2() == False:
        clear()
        print(Fore.CYAN + 'No one wins.' + Fore.WHITE)
    print('\ntable =\n' + Fore.LIGHTMAGENTA_EX + f'{table}' + Fore.WHITE)

def ChangeValue(New, Old):
    for i in range(3):
        if New[i] == 2:
            Old[0, i] = New[i]
    for i in range(3):
        if New[i + 3] == 2:
            Old[1, i] = New[i + 3]
    for i in range(3):
        if New[i + 6] == 2:
            Old[2, i] = New[i + 6]

def GameChoose():
    clear()
    print(Fore.LIGHTMAGENTA_EX + 'Hello. Please choose the type of game: ' + Fore.WHITE)
    x = input(Fore.LIGHTCYAN_EX + '\n1- Play 1v1\n2- Play with computer(Coming soon): ' + Fore.WHITE)
    match x:
        case '1':
            clear()
            GameStarter()
        case '2':
            clear()
            Loading()
        case _:
            clear()
            exit(0)

def GameStarter():
    A, B = Fore.YELLOW + player1, Fore.YELLOW + player2
    a, b = 'number of player1 is 1', 'number of player2 is 2.'
    c = 'You can press 1 to read help, 2 to start game else exit: '
    print(Fore.MAGENTA + 'Hi. wellcome to our game ' + A + Fore.MAGENTA + ' and ' + B)
    print(Fore.GREEN + f'In this game {a} and {b}')
    print(Fore.LIGHTCYAN_EX + 'Thank you for choosing our game. Good luck!\n')
    X = int(input(Fore.LIGHTRED_EX + c + Fore.WHITE))
    match X:
        case 1:
            clear()
            HelpOfGame()
            Playing()
        case 2:
            clear()
            Playing()
        case _:
            clear()
            exit(0)

def HelpOfGame():
    a = 'If you understand the help'
    c = 'press 1 to continue, else exit: '
    print(Fore.LIGHTGREEN_EX + f'Table = \n{table}\n')
    print(Fore.YELLOW + 'Left\tMiddle\t  Right')
    print(Fore.LIGHTMAGENTA_EX + '0, 0\t0, 1\t  0, 2')
    print('1, 0\t1, 1\t  1, 2')
    print('2, 0\t2, 1\t  2, 2\n')
    b = int(input(Fore.CYAN + f'{a} {c}' + Fore.WHITE))
    match b:
        case 1:
            clear()
        case _:
            clear()
            exit(0)

def GameNotes():
    print(Fore.LIGHTWHITE_EX + 'Please read this notes:'.upper())
    print(Fore.RED + 'The starter will be selected randomly.')
    print(Fore.CYAN + 'You most be enter a 2-digit number.')
    print(Fore.GREEN + 'The first Number is row and the second one in colomn.')
    print(Fore.MAGENTA + 'Row and column most be 0, 1 or 2.\n' + Fore.WHITE)
    sleep(1)

def TextToStart():
    a = 'to start the game'
    txt = input(Fore.LIGHTYELLOW_EX + f'Enter 1 {a} else exit: ' + Fore.WHITE)
    match txt:
        case '1':
            clear()
        case _:
            clear()
            exit(0)

def Winner1():
    if table[0, 0] == 1 and table[0, 0] == table[0, 1] and table[0, 0] == table[0, 2]:
        return True
    elif table[0, 0] == 1 and table[0, 0] == table[1, 1] and table[0, 0] == table[2, 2]:
        return True
    elif table[0, 2] == 1 and table[0, 2] == table[1, 1] and table[0, 2] == table[2, 0]:
        return True
    elif table[1, 0] == 1 and table[1, 0] == table[1, 1] and table[1, 0] == table[1, 2]:
        return True
    elif table[2, 0] == 1 and table[2, 0] == table[2, 1] and table[1, 0] == table[2, 2]:
        return True
    elif table[0, 0] == 1 and table[1, 0] == table[0, 0] and table[0, 0] == table[2, 0]:
        return True
    elif table[0, 1] == 1 and table[1, 1] == table[0, 1] and table[0, 1] == table[2, 1]:
        return True
    elif table[0, 2] == 1 and table[1, 2] == table[0, 2] and table[0, 2] == table[2, 2]:
        return True
    else:
        return False

def Winner2():
    if table[0, 0] == 2 and table[0, 0] == table[0, 1] and table[0, 0] == table[0, 2]:
        return True
    elif table[0, 0] == 2 and table[0, 0] == table[1, 1] and table[0, 0] == table[2, 2]:
        return True
    elif table[0, 2] == 2 and table[0, 2] == table[1, 1] and table[0, 2] == table[2, 0]:
        return True
    elif table[1, 0] == 2 and table[1, 0] == table[1, 1] and table[1, 0] == table[1, 2]:
        return True
    elif table[2, 0] == 2 and table[2, 0] == table[2, 1] and table[1, 0] == table[2, 2]:
        return True
    elif table[0, 0] == 2 and table[1, 0] == table[0, 0] and table[0, 0] == table[2, 0]:
        return True
    elif table[0, 1] == 2 and table[1, 1] == table[0, 1] and table[0, 1] == table[2, 1]:
        return True
    elif table[0, 2] == 2 and table[1, 2] == table[0, 2] and table[0, 2] == table[2, 2]:
        return True
    else:
        return False

def Location():
    x1 = y1 = Num1 = 0
    x2 = y2 = Num2 = 0
    lst = [0, 1]
    i = np.random.choice(lst, p=[0.5, 0.5])
    if i == 0:
        k = 0
        print(Fore.LIGHTGREEN_EX + f'{player1} starts the game.\n' + Fore.WHITE)
    elif i == 1:
        k = 1
        print(Fore.LIGHTGREEN_EX + f'{player2} starts the game.\n' + Fore.WHITE)
    sleep(1)
    clear()
    while i < (9 + k):
        if Winner1() == True or Winner2() == True:
            break
        if i%2 == 0:
            print(Fore.WHITE + f'Table =\n{table}\n')
            n1 = int(input(Fore.YELLOW + f'Please enter a correct number {player1} {a}' + Fore.WHITE))
            x1, y1, Num1 = (n1 // 10) % 10, n1 % 10, 1
            if not(x1 > 2 or y1 > 2 or table[x1][y1] != 0):
                i += 1
                table[x1][y1] = Num1
                clear()
            else:
                clear()
                print('The value you entered is incorrect!')
                sleep(1.5)
                clear()
                print(f'Table =\n{table}\n')
                clear()
                continue
        else:
            print(Fore.WHITE + f'Table =\n{table}\n')
            n2 = int(input(Fore.CYAN + f'Please enter a correct number {player2} {a}' + Fore.WHITE))
            x2, y2, Num2 = (n2 // 10) % 10, n2 % 10, 2
            if not(x2 > 2 or y2 > 2 or table[x2][y2] != 0):
                i += 1
                table[x2][y2] = Num2
                clear()
            else:
                clear()
                print('The value you entered is incorrect!')
                sleep(1.5)
                clear()
                print(f'Table =\n{table}\n')
                clear()
                continue

        if x1 > 2 or y1 > 2 or (Num1 != 1 and Num1 != 2):
            clear()
            continue
        if x2 > 2 or y2 > 2 or (Num2 != 1 and Num2 != 2):
            clear()
            continue
    if Winner1() == True:
        clear()
        print(Fore.CYAN + f'{player1} wins.' + Fore.WHITE)
    if Winner2() == True:
        clear()
        print(Fore.CYAN + f'{player2} wins.' + Fore.WHITE)
    if Winner1() == False and Winner2() == False:
        clear()
        print(Fore.CYAN + 'No one wins.' + Fore.WHITE)
    print('\ntable =\n' + Fore.LIGHTMAGENTA_EX + f'{table}' + Fore.WHITE)

def Playing():
    GameNotes()
    TextToStart()
    Location()

player1 = input(Fore.YELLOW + 'Please enter the first player name: ')
player2 = input(Fore.LIGHTGREEN_EX + 'Please enter the second player (or bot) name: ')
a = '(Row and colomn): '
table = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
GameChoose()