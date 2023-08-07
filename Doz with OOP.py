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

class Player:
    Ptype = True
    def __init__(self):
        pass

    def Initiate(self):
        self.name = input("Enter player's name: ")
        self.priority = np.random.choice([0, 1], p=[0.5, 0.5])

p1, p2 = Player(), Player()
p1.Initiate()
p2.Initiate()

clear()
print(f'Hello and welcome {p1.name} and {p2.name}.\n')
sleep(1)

class Game:
    table = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    def __init__(self):
        pass

    def Help(self):
        a = 'If you understand the help'
        c = 'press 1 to continue, else exit: '
        print(Fore.LIGHTGREEN_EX + f'Table = \n{self.table}\n')
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

    def Notes(self):
        print(Fore.LIGHTWHITE_EX + 'Please read this notes before choosing the type of game:'.upper())
        print(Fore.RED + 'The starter will be selected randomly.')
        print(Fore.CYAN + 'You most be enter a 2-digit number.')
        print(Fore.GREEN + 'The first Number is row and the second one in colomn.')
        print(Fore.MAGENTA + 'Row and column most be 0, 1 or 2.\n' + Fore.WHITE)
        sleep(1)
        self.con = int(input('Now you can press 1 to continue: '))

    def Mode(self):
        print('Now please choose the mode.\nMode 1: 1v1\nMode 2: vs bot')
        self.x = int(input('Mode? '))
        if self.x == 1:
            p2.Ptype = True
        elif self.x == 2:
            p2.Ptype = False

    def Movement(self):
        pass

g = Game()
g.Notes()

if g.con == 1:
    clear()
    g.Mode()
else:
    clear()
    exit(0)