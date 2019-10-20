
#


def playPerson(player, table, passNum):
    print('Is The Turn Of: ', player.name)
    input('Press Enter To Continue')
    print(player.name, ' Tokens: ')
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):

        # points for pass other players
        if passNum[0] == 3:
            table.passOtherPlayers()

        passNum[0] = 0
        print('You can play a token')
        print('Enter the number: ', end='')
        token = input()
        while not player.addTokenToTable(token, table):
            print('Enter a valid token: ', end='')
            token = input()
        print(player.name + ' Has played: ' + token)
        return [player, token]
    else:
        print('You can not play a token')
        input('Press enter to Pass')
        player.passTurn()
        passNum[0] += 1
        print(player.name + ' Has: Passed')
        return [player, 'Passed']


def playBot(player, table, handPlay, passNum):
    # print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        # win x points
        token = player.autoPlay(table)
        passNum[0] = 0
        handPlay.currentRound.append([player, token])
        # print(player.name + ' has played: ')
    else:
        player.passTurn()
        passNum[0] += 1
        print(player.name + ' Has: Passed')
        handPlay.currentRound.append([player, 'Passed'])
