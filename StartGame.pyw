#

import os
from Clases import ClassGame as CGame, ClassHandPlay as CHandPlay, ClassPlayer as Cplayer
from Actions.PlayerActions import playPerson, playBot
from Reports import report

# introduction

# MENU

# make control for each input


def Pycls(): return os.system("cls")  # cls, borrar pantalla


Pycls()
print('welcome to ... dominoes game')
print('iniciacion para jugar')
print()
AllGames = {}

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

    report(AllGames[p1])

    print('comienzo del juego')
    
    if AllGames[p1].handPlays[-1].handPlayNumber == 1:
        token = AllGames[p1].handPlays[-1].openDoubleSix()
        AllGames[p1].addToken(token)
        for player in AllGames[p1].handPlays[-1].players[1:]:
            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].handPlays[-1])
            else:
                playPerson(player, AllGames[p1], AllGames[p1].handPlays[-1])

    while AllGames[p1].handPlays[-1].winner is None:

        report(AllGames[p1])

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
