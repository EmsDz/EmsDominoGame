
#
import os


def Pycls():
    return os.system("cls")


def menu():
    print("This will be the menu part, coming soon :) ;)")


def playerSelector(playerList, Bots, Enterp):
    print("select one of the options below:")
    print('1- bot vs bot')
    print('2- player vs bot')
    print('3- player vs player')
    print('4- 3 to 4 players')

    while True:
        selected = input('\nyour selection is: ')
        Pycls()
        # selected
        if selected in "1234":
            break
        else:
            print('wrong number, enter again.')

    # selected 1-
    if selected == '1':
        playerList.append(Bots.pop())
        playerList.append(Bots.pop())

    # selected 2-
    if selected == '2':
        playerList.append(Bots.pop())
        playerList.append(Enterp.player(input('enter name of player: ')))

    # selected 3-
    if selected == '3':
        playerList.append(Enterp.player(input('enter name of player 1: ')))
        playerList.append(Enterp.player(input('enter name of player 2: ')))

    # selected 4-
    while selected == '4':
        nPlayers = int(input('enter number of player, between 2 and 4: '))
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
