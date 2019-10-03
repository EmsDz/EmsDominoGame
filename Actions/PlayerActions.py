#

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
        