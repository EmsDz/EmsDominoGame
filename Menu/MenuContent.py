
#
import os
from .Introduction import introduction as intro

def Pycls():
    return os.system("cls")


def menu():
    Pycls()
    intro()
    # print("")
    print("Select an obtion:")
    print("1- Play Dominoes")
    # print("2- Dominoes Rules")
    print("2- Exit Game")
    # print("")
    selected = input("\nYour selectionis: ")
    while selected not in ['1','2'] or selected == '':
        Pycls()
        print('\n\nWrong number, Enter again.\n')
        return menu()

    if selected == '2':
        while True:
            Pycls()
            p = input('\n\nYou realy want to exit? YES/NO \nYour answer: ').upper()
            if p in ['N','NO']:
                return menu()
            if p in ['Y', 'YES']:
                break
        return selected


def playerSelector(playerList, Bots, Enterp):
    print("Select one of the options below:")
    print('1- Bot vs Bot')
    print('2- Player vs Bot')
    print('3- Player vs Player')
    print('4- 3 to 4 Players')

    while True:
        selected = input('\nYour selection is: ')
        # Pycls()
        # selected
        if selected in ["1","2", "3", "4"] and selected != '':
            break
        else:
            print('Wrong number, Enter again.\n')
            playerSelector(playerList, Bots, Enterp)

    # selected 1-
    if selected == '1':
        playerList.append(Bots.pop())
        playerList.append(Bots.pop())

    # selected 2-
    if selected == '2':
        playerList.append(Bots.pop())
        playerList.append(Enterp.player(input('Enter name of player: ')))

    # selected 3-
    if selected == '3':
        playerList.append(Enterp.player(input('Enter name of player 1: ')))
        playerList.append(Enterp.player(input('Enter name of player 2: ')))

    # selected 4-
    while selected == '4':
        nPlayers = int(input('Enter number of player, Between 2 and 4: '))
        if nPlayers >= 2 and nPlayers <= 4:
            for x in range(0, nPlayers):
                yesOrno = input('want a bot player: yes or no ').upper()
                if yesOrno == 'YES':
                    playerList.append(Bots.pop())
                elif yesOrno == 'NO':
                    playerList.append(Enterp.player(input('enter name of player: ')))
                else:
                    print("enter a valid input.")
                    nPlayers += 1
        break
    return