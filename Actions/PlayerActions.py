
#


def pickToken(player, table):
    if table.tokenPit:
        player.getTokenFromTokenPit(table)
        if not player.checkPlay(table):
            pickToken(player, table)
        return
    else:
        print('Token Pit is empty.')
        return


def playPerson(player, table, passNum):
    print('Is The Turn Of: ', player.name)
    print(player.name, ' Tokens: ', end='')
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])

    if player.checkPlay(table):
        if passNum[0] == 3:  # change
            print('You win x points')

        passNum[0] = 0
        print('You can play a token')
        token = input('Enter the number: ')

        # check if is a valid token
        while token not in player.tokens and token[::-1] not in player.tokens:
            token = input('Enter a valid token: ')

        while player.addTokenToTable(token, table):
            print('Enter a playable token: ')

        print(player.name + ' Has played: ' + player.tokens[token].number)
        table.handPlays[-1].currentRound.append([player, player.tokens[token].number])

        try:
            player.tokens.pop(token.number)
        except Exception:
            player.tokens.pop(token.number[::-1])
        return
    # elif table.tokenPit:
    #     pass
    else:
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
        token = player.autoPlay(table)
        passNum[0] = 0
        table.handPlays[-1].currentRound.append([player, token])
        return
    elif table.tokenPit:
        while table.tokenPit and not player.checkPlay(table):
            table.giveFromTokenPit(player)
        else:
            playBot(player, table, handPlay, passNum)
            return
    else:
        player.passTurn()
        passNum[0] += 1
        print(player.name + ' Has: Passed')
        table.handPlays[-1].currentRound.append([player, 'Passed'])
        return
