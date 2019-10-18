
#


def playPerson(player, table, passNum):
    print('Is The Turn Of: ', player.name)
    input('Press Enter To Continue')
    print(player.name, ' Tokens: ')
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        if passNum[0] == 3:  # change
            print('You win x points')
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
        token = player.autoPlay(table, handPlay)
        passNum[0] = 0
        handPlay.currentRound.append([player, token])
        # print(player.name + ' has played: ')
    else:
        player.passTurn()
        passNum[0] += 1
        print(player.name + ' Has: Passed')
        handPlay.currentRound.append([player, 'Passed'])
