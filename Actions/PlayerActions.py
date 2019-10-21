
#


def pickToken(player, table):
    if table.tokenPit:
        player.getTokenFromTokenPit(table)
        if not player.checkPlay(table):
            pickToken(player, table)
        return True
    else:
        print('Token Pit is empty.')
        return False


def playPerson(player, table, passNum):
    print('Is The Turn Of: ', player.name)
    player.showPlayerTokens()

    if player.checkPlay(table):

        # points for pass other players
        if passNum[0] == 3:
            table.passOtherPlayers()

        passNum[0] = 0
        print('You can play a token')
        token = input('Enter the number: ')

        # check if is a valid token
        while not player.addTokenToTable(token, table):
            table.Pycls()
            table.showTableTokens()
            player.showPlayerTokens()
            token = input('Enter a valid token: ')

        if token not in player.tokens:
            player.tokens.pop(token[::-1])
        else:
            player.tokens.pop(token)

        table.Pycls()
        print(player.name + ' Has played: ' + token)
        table.handPlays[-1].currentRound.append([player, token])

        return
    elif table.tokenPit:
        print('You do not have token to play.')
        input('You will pick one until you can play or pass. Enter')
        if pickToken(player, table):
            table.Pycls()
            table.showTableTokens()
            table.handPlays[-1].showHandLog()
            print('Now you can play a token.')
            playPerson(player, table, passNum)
            return

    # pass the turn
    print('You can not play a token')
    input('Press enter to Pass')
    player.passTurn()
    passNum[0] += 1
    print(player.name + ' Has: Passed')
    table.handPlays[-1].currentRound.append([player, 'Passed'])
    return


def playBot(player, table, passNum):
    # print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        # win x points
        player.autoPlay(table)
        passNum = [0]
        return
    elif table.tokenPit:
        while table.tokenPit and not player.checkPlay(table):
            table.giveFromTokenPit(player)
        else:
            playBot(player, table, passNum)
            return
    # pass the turn
    player.passTurn()
    passNum[0] += 1
    print(player.name + ' Has: Passed')
    table.handPlays[-1].currentRound.append([player, 'Passed'])
    return
