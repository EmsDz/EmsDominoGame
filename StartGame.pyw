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

    # Pycls()

    # report(AllGames[p1])

    print('comienzo del juego')
    
    if AllGames[p1].handPlays[-1].handPlayNumber == 1:
        token = AllGames[p1].handPlays[-1].openDoubleSix()
        AllGames[p1].addToken(token)
        for player in AllGames[p1].handPlays[-1].players[1:]:
            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].handPlays[-1], AllGames[p1].passCount)
            else:
                playPerson(player, AllGames[p1], AllGames[p1].passCount)

    while AllGames[p1].handPlays[-1].winner is None:

        # report(AllGames[p1])

        # if AllGames[p1].handPlays[-1].handPlayNumber == 1:
        #     openDoubleSix(AllGames[p1].handPlays[-1].players[0])

        for player in AllGames[p1].handPlays[-1].players:
            print("Mesa: ")
            [token.showToken() for token in AllGames[p1].tokens]
            print()  # [token.showToken() for token in AllGames[p1].tokens])

            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].handPlays[-1], AllGames[p1].passCount )
            else:
                playPerson(player, AllGames[p1], AllGames[p1].passCount)

            AllGames[p1].handPlayBlocked(player)

            if AllGames[p1].handPlays[-1].checkWinner(player, AllGames[p1]):
                AllGames[p1].clearTable()
                AllGames[p1].clearPlayerTokens(AllGames[p1].handPlays[-1].players)
                print('end of the game')
                print('the winner is: ', AllGames[p1].handPlays[-1].winner)

            # input('\npress enter')
            # Pycls()

    print('end of game? NO. is end of handPlay')
    input('enter')
