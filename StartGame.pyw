#

import os
from Clases import ClassGame as CGame, ClassHandPlay as CHandPlay, ClassPlayer as Cplayer

# introduction

# MENU

# make control for each input


def Pycls(): return os.system("cls")  # cls, borrar pantalla


Pycls()
print('welcome to ... dominoes game')
print('iniciacion para jugar')
print()
AllGames = {}


def playPerson(player, table, handPlay):
    print('is the turn of: ', player.name)
    input('press enter to continue')
    print(player.name, ' tokens: ')
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        print('you can play a token')
        print('enter the number: ', end='')
        while not player.addTokenToTable(input(), table):
            print('enter a valid token: ', end='')
        if handPlay.passCount == 3:  # poner mas arriba
            print('you win x points')
        handPlay.passCount = 0
    else:
        print('you can not play a token')
        input('press enter to pass')
        player.passTurn()
        handPlay.passCount += 1


def playBot(player, table, handPlay):
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        player.autoPlay(table)
        handPlay.passCount = 0
    else:
        player.passTurn()
        handPlay.passCount += 1


def Reports(table):
    print('')
    print('Reports: ')
    print('players name: ', table.playerList[0].name + ', ', end=''),
    print(table.playerList[1].name + ', ' + table.playerList[2].name + ', ', end='')
    print(table.playerList[3].name, '\n')
    print(table.playerList[0].name + ' : ', [token for token in table.playerList[0].tokens])
    print(table.playerList[1].name + ' : ', [token for token in table.playerList[1].tokens])
    print(table.playerList[2].name + ' : ', [token for token in table.playerList[2].tokens])
    print(table.playerList[3].name + ' : ', [token for token in table.playerList[3].tokens], '\n')
    print('hand plays', len(table.handPlays))
    print('current hand Play: ', table.handPlays[-1].handPlayNumber, '\n')
    print('first player: ', table.handPlays[-1].firstsTurn)
    print('play order: ', [player.name for player in table.handPlays[-1].players])
    input('waiting for key...')


def openDoubleSix(players):
    for player in AllGames[p1].handPlays[-1].players:
        [token.showToken() for token in AllGames[p1].tokens]
        print()  # [token.showToken() for token in AllGames[p1].tokens])

        if player.imAbot:
            playBot(player, AllGames[p1], AllGames[p1].handPlays[-1])
        else:
            playPerson(player, AllGames[p1], AllGames[p1].handPlays[-1])


while input('continue with the game: ').upper() == 'S':

    if input('create new game: ') == 's':
        p1 = len(AllGames) + 1
        AllGames[p1] = CGame.game()
        AllGames[p1].makeTokenBox()

    if True:  # input('create players: ') == 's':
        nPlayers = int(input('enter number of player: '))
        for x in range(0, nPlayers):
            #     # AllGames[p1].playerList.append(Cplayer.player(input('enter name: ')))
            AllGames[p1].playerList.append(AllGames[p1].Bots.pop())

        AllGames[p1].shuffleTokens(AllGames[p1].tokenBox)
        AllGames[p1].giveTokens(AllGames[p1].playerList)

    if True:  # input('create hand play: ') == 's':
        AllGames[p1].newHandPlay(CHandPlay.handPlay(AllGames[p1].playerList))
        AllGames[p1].handPlays[-1].makeFirstsTurn()
        AllGames[p1].handPlays[-1].makePlayOrder()

    Pycls()

    Reports(AllGames[p1])

    print('comienzo del juego')

    while AllGames[p1].handPlays[-1].winner is None:

        Reports(AllGames[p1])

        # if AllGames[p1].handPlays[-1].handPlayNumber == 1:
        #     openDoubleSix(AllGames[p1].handPlays[-1].players[0])

        for player in AllGames[p1].handPlays[-1].players:
            [token.showToken() for token in AllGames[p1].tokens]
            print()  # [token.showToken() for token in AllGames[p1].tokens])

            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].handPlays[-1])
            else:
                playPerson(player, AllGames[p1], AllGames[p1].handPlays[-1])

            if AllGames[p1].handPlays[-1].passCount == 4:
                print('end of the game')  # with the 2 next players
            # elif AllGames.[p1].handPlays[-1].passCount == 3:
            #     print('you win x points for pass all players')  # is the next player

            if AllGames[p1].handPlays[-1].checkWinner(player, AllGames[p1]):
                AllGames[p1].clearTable()
                AllGames[p1].clearPlayerTokens(AllGames[p1].handPlays[-1].players)
                print('end of the game')
                print('the winner is: ', AllGames[p1].handPlays[-1].winner)

            # input('\npress enter')
            Pycls()

    print('end of game? NO. is end of handPlay')
    input('enter')
