
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
    while selected not in ['1', '2'] or selected == '':
        Pycls()
        print('\n\nWrong number, Enter again.\n')
        return menu()

    if selected == '2':
        while True:
            Pycls()
            p = input('\n\nYou realy want to exit? YES/NO \nYour answer: ').upper()
            if p in ['N', 'NO']:
                return menu()
            if p in ['Y', 'YES']:
                break
        return selected


def partners(groups):
    # groups 1
    groups[0].partner = groups[2].name
    groups[2].partner = groups[0].name
    # group
    groups[1].partner = groups[3].name
    groups[3].partner = groups[1].name


def makeGroups(playerN):
    selected = ''
    while selected not in ['YES', 'Y', 'NO', 'NOT', 'N']:
        Pycls()
        selected = input('\n\nWant to play in groups? Yes/No\nYour choice: ').upper()

    if selected in ['YES', 'Y']:
        selected = '0'
        while selected not in ['1', '2', '3']:
            Pycls()
            print('\n\nValid teams:')
            print('1- ', playerN[0].name, '-', playerN[1].name, ' vs ', playerN[2].name, '-', playerN[3].name)
            print('2- ', playerN[0].name, '-', playerN[2].name, ' vs ', playerN[3].name, '-', playerN[1].name)
            print('3- ', playerN[0].name, '-', playerN[3].name, ' vs ', playerN[1].name, '-', playerN[2].name)
            selected = input('Select teams: ')

        # team 1 vs team 2 = position in table: playerteam1 - playerteam2 - playerteam1 - playerteam2
        if selected == '1':
            playerN = [playerN[0], playerN[2], playerN[1], playerN[3]]
            partners(playerN)
        elif selected == '2':
            playerN = [playerN[0], playerN[3], playerN[2], playerN[1]]
            partners(playerN)
        else:
            playerN = [playerN[0], playerN[1], playerN[3], playerN[2]]
            partners(playerN)


def playerSelector(playerList, Bots, CreatePlayer):
    Pycls()
    print("\n\nSelect one of the options below:")
    print('1- Bot vs Bot')
    print('2- Player vs Bot')
    print('3- Player vs Player')
    print('4- 3 to 4 Players')

    while True:
        selected = input('\nYour selection is: ')
        # Pycls()
        # selected
        if selected in ["1", "2", "3", "4"] and selected != '':
            break
        else:
            input('Wrong number, Enter again. Press enter to continue\n')
            playerSelector(playerList, Bots, CreatePlayer)

    # selected 1-
    if selected == '1':
        playerList.append(Bots.pop())
        playerList.append(Bots.pop())

    # selected 2-
    if selected == '2':
        playerList.append(Bots.pop())
        playerList.append(CreatePlayer.player(input('Enter name of player: ')))

    # selected 3-
    if selected == '3':
        playerList.append(CreatePlayer.player(input('Enter name of player 1: ')))
        playerList.append(CreatePlayer.player(input('Enter name of player 2: ')))

    # selected 4-
    while selected == '4':
        nPlayers = int(input('Enter number of player, Between 2 and 4: '))
        if nPlayers >= 2 and nPlayers <= 4:
            for x in range(0, nPlayers):
                Pycls()
                print('\n\nPlayer #', len(playerList))
                yesOrno = input('Want a bot player: Yes or No\nYour choice: ').upper()
                if yesOrno in ['YES', 'Y']:
                    playerList.append(Bots.pop())
                elif yesOrno in ['NO', 'N']:
                    playerList.append(CreatePlayer.player(input('Enter name of player: ')))
                else:
                    input("Enter a valid input.")
                    nPlayers += 1

            # the player if wants select a partner and make group
            if nPlayers == 4:
                makeGroups(playerList)
        break
    return
