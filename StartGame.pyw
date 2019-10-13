#

import os
from Clases import ClassGame as CGame, ClassHandPlay as CHandPlay, ClassPlayer as Cplayer
from Actions.PlayerActions import playPerson, playBot
from Menu import Introduction as Intro, MenuContent as MenuC
from Reports import report


# make control for each input

def Pycls(): return os.system("cls")  # cls, borrar pantalla


Pycls()
Intro.introduction()
MenuC.menu()
print('iniciacion para jugar')
print()
AllGames = {}


def playerTurn(player, playerList):
    nextplayer = playerList.index(player) + 1
    input('es turno de: ' + playerList[nextplayer].name)


while input('continue with the game: ').upper() == 'S':

    if input('create new game: ') == 's':
        p1 = len(AllGames) + 1
        AllGames[p1] = CGame.game()
        AllGames[p1].makeTokenBox()

    # create players and bots
    if True:  # input('create players: ') == 's':
        print("select: 1- bot vs bot, 2- player vs bot, 3- player vs player, 4- 3 to 4 players")
        while True:
            selected = input('your selection is: ')

            # selected 1-
            if selected == '1':
                AllGames[p1].playerList.append(AllGames[p1].Bots.pop())
                AllGames[p1].playerList.append(AllGames[p1].Bots.pop())

            # selected 2-
            if selected == '2':
                AllGames[p1].playerList.append(AllGames[p1].Bots.pop())
                AllGames[p1].playerList.append(Cplayer.player(input('enter name of player: ')))

            # selected 3-
            if selected == '3':
                AllGames[p1].playerList.append(Cplayer.player(input('enter name of player 1: ')))
                AllGames[p1].playerList.append(Cplayer.player(input('enter name of player 2: ')))

            # selected 4-
            while selected == '4':
                nPlayers = int(input('enter number of player, between 2 and 4: '))
                if nPlayers >= 2 and nPlayers <= 4:
                    for x in range(0, nPlayers):
                        yesOrno = input('want a bot player: yes or no ').upper()
                        if yesOrno == 'YES':
                            AllGames[p1].playerList.append(AllGames[p1].Bots.pop())
                        elif yesOrno == 'NO':
                            AllGames[p1].playerList.append(Cplayer.player(input('enter name of player: ')))
                        else:
                            print("enter a valid input.")
                            nPlayers += 1
                        break

            # selected

            if selected in "1234":
                break

# loop of game

        AllGames[p1].shuffleTokens(AllGames[p1].tokenBox)
        AllGames[p1].giveTokens(AllGames[p1].playerList)

    if True:  # input('create hand play: ') == 's':
        AllGames[p1].newHandPlay(CHandPlay.handPlay(AllGames[p1].playerList))
        AllGames[p1].handPlays[-1].makeFirstsTurn()
        AllGames[p1].handPlays[-1].makePlayOrder()

    Pycls()

    # report(AllGames[p1])

    print('comienzo del juego')

    if AllGames[p1].handPlays[-1].handPlayNumber == 1:
        AllGames[p1].showTableToken()
        token = AllGames[p1].handPlays[-1].openDoubleSix()
        AllGames[p1].addToken(token)
        playerTurn(AllGames[p1].handPlays[-1].players[0], AllGames[p1].handPlays.players)
        for player in AllGames[p1].handPlays[-1].players[1:]:
            Pycls()
            AllGames[p1].showTableToken()
            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].handPlays[-1], AllGames[p1].passCount)
            else:
                playPerson(player, AllGames[p1], AllGames[p1].passCount)
            playerTurn(player, AllGames[p1].handPlays.players)

    while AllGames[p1].handPlays[-1].winner is None:

        # report(AllGames[p1])

        # if AllGames[p1].handPlays[-1].handPlayNumber == 1:
        #     openDoubleSix(AllGames[p1].handPlays[-1].players[0])

        for player in AllGames[p1].handPlays[-1].players:
            Pycls()
            AllGames[p1].showTableToken()

            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].handPlays[-1], AllGames[p1].passCount)
            else:
                playPerson(player, AllGames[p1], AllGames[p1].passCount)

            AllGames[p1].handPlayBlocked(player)

            if AllGames[p1].handPlays[-1].checkWinner(player, AllGames[p1]):
                AllGames[p1].clearTable()
                AllGames[p1].clearPlayerTokens(AllGames[p1].handPlays[-1].players)
                print('end of the game')
                print('the winner is: ', AllGames[p1].handPlays[-1].winner)
                break

            playerTurn(player, AllGames[p1].handPlays.players)

    input('\npress enter')
    Pycls()
    print('New handPlay')

    # print('end of game? NO. is end of handPlay')
    input('enter')
