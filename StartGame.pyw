
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
AllGames = {}


def playerTurn(player, playerList):
    nextplayer = playerList.index(player) + 1
    if nextplayer >= len(playerList):
        nextplayer = 0

    input('Is Turn Of: ' + playerList[nextplayer].name)


def playersRound(players):
    for player in players:
        Pycls()
        AllGames[p1].showTableTokens()
        if player.imAbot:
            playBot(player, AllGames[p1], AllGames[p1].handPlays[-1], AllGames[p1].passCount)
        else:
            data = playPerson(player, AllGames[p1], AllGames[p1].passCount)
            AllGames[p1].handPlays[-1].currentRound.append(data)

        if AllGames[p1].handPlays[-1].checkWinner(player, AllGames[p1]) or AllGames[p1].blockedWin(player):
            AllGames[p1].clearTable()
            AllGames[p1].clearPlayerTokens(AllGames[p1].handPlays[-1].players)
            print('End of the hand')
            print('The winner is: ', AllGames[p1].handPlays[-1].winner)
            break
        playerTurn(player, AllGames[p1].handPlays[-1].players)


while input('Wants to play Dominoes?, Yes/No: ').upper() == 'YES':

    if input('Create Game?, Yes/No: ').upper() == 'YES':
        p1 = len(AllGames) + 1
        AllGames[p1] = CGame.game()
        AllGames[p1].makeTokenBox()
    else:
        print('Thanks, buelbe cuando quieras jugar')

    # create players and bots
    if not AllGames[p1].playerList:
        Pycls()
        MenuC.playerSelector(AllGames[p1].playerList, AllGames[p1].Bots, Cplayer)

    print('Game Start')

# loop of game
    while AllGames[p1].gameHasEnded is False:

        AllGames[p1].shuffleTokens(AllGames[p1].tokenBox)
        AllGames[p1].giveTokens(AllGames[p1].playerList)

        AllGames[p1].newHandPlay(CHandPlay.handPlay(AllGames[p1].playerList))
        AllGames[p1].handPlays[-1].handPlayNumber = len((AllGames[p1].handPlays))

        # Temporary Logs
        LogState1 = AllGames[p1].handPlays[-1].currentRound
        LogState2 = AllGames[p1].handPlays[-1].handPlayLog

        if len(AllGames[p1].handPlays) == 1:
            AllGames[p1].handPlays[-1].makeFirstsTurn()
        else:
            AllGames[p1].handPlays[-1].firstsTurn = AllGames[p1].handPlays[-2].winner

        AllGames[p1].handPlays[-1].makePlayOrder()

        Pycls()

        if AllGames[p1].handPlays[-1].handPlayNumber == 1:
            print('Hand Start')
            AllGames[p1].showTableTokens()
            token = AllGames[p1].handPlays[-1].openDoubleSix()
            AllGames[p1].addToken(token)
            playerTurn(AllGames[p1].handPlays[-1].players[0], AllGames[p1].handPlays[-1].players)

            # log registry
            AllGames[p1].handPlays[-1].currentRound.append([AllGames[p1].handPlays[-1].players[0], token])

            playersRound(AllGames[p1].handPlays[-1].players[1:])
            AllGames[p1].handPlays[-1].handPlayLog[1] = AllGames[p1].handPlays[-1].currentRound
            AllGames[p1].handPlays[-1].currentRound = []

        # temporary variable
        logCount = 2
        while AllGames[p1].handPlays[-1].winner is None:
            playersRound(AllGames[p1].handPlays[-1].players)
            AllGames[p1].handPlays[-1].handPlayLog[logCount] = AllGames[p1].handPlays[-1].currentRound
            AllGames[p1].handPlays[-1].currentRound = []
            logCount += 1

        print('hand prints: ', AllGames[p1].handPlays[-1].points)
        print('p1: ', AllGames[p1].handPlays[-1].players[0].name, AllGames[p1].handPlays[-1].players[0].playerPoints)
        print('p2: ', AllGames[p1].handPlays[-1].players[1].name, AllGames[p1].handPlays[-1].players[1].playerPoints)

        input('\nPress Enter')
        Pycls()
        print('New handPlay')

        # end of the game
        endGame = AllGames[p1].endOfGame(AllGames[p1].handPlays[-1].players)

        if endGame[0] is True:
            print('The Game has ended.')
            if type(endGame[1]) is list:
                print('Te Winners are: ', endGame[1][0], endGame[1][1])
            else:
                print('Te Winner is: ', endGame[1])
            input('')
