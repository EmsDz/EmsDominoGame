#


def playPerson(player, table, passNum):
    print('is the turn of: ', player.name)
    input('press enter to continue')
    print(player.name, ' tokens: ')
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        if passNum[0] == 3:
            print('you win x points')
        passNum[0] = 0
        print('you can play a token')
        print('enter the number: ', end='')
        token = input()
        while not player.addTokenToTable(token, table):
            print('enter a valid token: ', end='')
            token = input()
        print(player.name + ' has played: ' + token)
    else:
        print('you can not play a token')
        input('press enter to pass')
        player.passTurn()
        passNum[0] += 1
        print(player.name + ' has played: passed')


def playBot(player, table, handPlay, passNum):
    print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
    if player.checkPlay(table):
        player.autoPlay(table, handPlay)
        passNum[0] = 0
        # print(player.name + ' has played: ')
    else:
        player.passTurn()
        passNum[0] += 1
        print(player.name + ' has played: passed')
