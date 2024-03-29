
#

from Clases import ClassGame as CGame, ClassHandPlay as CHandPlay, ClassPlayer as Cplayer
from Actions.PlayerActions import playPerson, playBot
from Menu import Introduction as Intro, MenuContent as MenuC
from Reports import report


# Part of the menu
MenuC.Pycls()
AllGames = {}  # content all games that can be created


def playerTurn(player, playerList):
    # AllGames[p1].Pycls()
    nextplayer = playerList.index(player) + 1
    if nextplayer >= len(playerList):
        nextplayer = 0

    input('Is Turn Of: ' + playerList[nextplayer].name)


def playersRound(players):
    for player in players:
        AllGames[p1].Pycls()

        AllGames[p1].showTableTokens()
        AllGames[p1].handPlays[-1].showHandLog()

        if not AllGames[p1].tokens:
            token = AllGames[p1].handPlays[-1].openHandPlay(player)
            # ended game
            if token == 'EXIT':
                return 'EXIT'

            AllGames[p1].handPlays[-1].currentRound.append([player, token.number])
            AllGames[p1].addToken(token)
        else:
            # check for the player
            if player.imAbot:
                playBot(player, AllGames[p1], AllGames[p1].passCount)
            else:
                exit = playPerson(player, AllGames[p1], AllGames[p1].passCount)
                # ended game
                if exit == 'EXIT':
                    return 'EXIT'

        # check if the hand has ended, normal or blocked
        if not player.tokens:
            AllGames[p1].Pycls()
            AllGames[p1].normalWin(player)
            break
        elif AllGames[p1].handIsBlocked():
            AllGames[p1].Pycls()
            AllGames[p1].blockedWin(player)
            break

        playerTurn(player, AllGames[p1].handPlays[-1].players)
    return ''


while True:

    selectect = MenuC.menu()

    if selectect == '2':
        print('\n\nThanks, hope you return later')
        print("You close the Game.\n\n")
        break

    # create the game
    p1 = len(AllGames) + 1
    AllGames[p1] = CGame.game()
    AllGames[p1].makeTokenBox()

    # create players and bots
    if not AllGames[p1].playerList:
        AllGames[p1].Pycls()
        MenuC.playerSelector(AllGames[p1].playerList, AllGames[p1].Bots, Cplayer)

# loop of game
    while AllGames[p1].gameHasEnded is False:

        AllGames[p1].shuffleTokens(AllGames[p1].tokenBox)
        AllGames[p1].giveTokens(AllGames[p1].playerList)

        # Create Hand Play
        AllGames[p1].newHandPlay(CHandPlay.handPlay(AllGames[p1].playerList))

        # manage the first player in each hand
        if len(AllGames[p1].handPlays) == 1:
            AllGames[p1].handPlays[-1].makeFirstsTurn()  # for the 1fr hand
        else:
            AllGames[p1].handPlays[-1].firstsTurn = AllGames[p1].handPlays[-2].winner  # for other hands

        AllGames[p1].handPlays[-1].makePlayOrder()

        # temporary variable
        logCount = 1

        while AllGames[p1].handPlays[-1].winner is None:
            exit = playersRound(AllGames[p1].handPlays[-1].players)
            # ended game
            if exit == 'EXIT':
                break

            # log registry
            AllGames[p1].handPlays[-1].handPlayLog[logCount] = AllGames[p1].handPlays[-1].currentRound.copy()
            AllGames[p1].handPlays[-1].currentRound = []
            logCount += 1
        # ended game
        if exit == 'EXIT':
            break

        print('\nHand Points: ', AllGames[p1].handPlays[-1].points, '\n')
        for player in AllGames[p1].handPlays[-1].players:
            print(player.name, ' points: ', player.playerPoints)

        input('\nPress Enter')
        AllGames[p1].Pycls()

        # end of the game
        endGame = AllGames[p1].endOfGame(AllGames[p1].handPlays[-1].players)

        if endGame[0] is True:
            print('\n\nThe Game has ended.\n')
            if type(endGame[1]) is list:
                print('*** Te Winners are: ', endGame[1][0], endGame[1][1])
            else:
                print('*** Te Winner is: ', endGame[1])
            input('\nPress Enter')

    AllGames[p1].Pycls()

    # ended game
    if exit == 'EXIT':
        print('\n\nYou Ended the Game.')
        input('\n\nPress Enter to continue...')

# controls
