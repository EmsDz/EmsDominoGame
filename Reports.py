#

def report(table):
    print('')
    print('Reports: ')
    print('players name: ', table.playerList[0].name + ', ', end=''),
    print(table.playerList[1].name + ', ' + table.playerList[2].name + ', ', end='')
    print(table.playerList[3].name, '\n')
    
    print('players tokens: ')
    print(table.playerList[0].name + ' : ', [token for token in table.playerList[0].tokens])
    print(table.playerList[1].name + ' : ', [token for token in table.playerList[1].tokens])
    print(table.playerList[2].name + ' : ', [token for token in table.playerList[2].tokens])
    print(table.playerList[3].name + ' : ', [token for token in table.playerList[3].tokens], '\n')
    
    print('hand plays', len(table.handPlays))
    print('current hand Play: ', table.handPlays[-1].handPlayNumber, '\n')
    
    print('first player: ', table.handPlays[-1].firstsTurn)
    print('play order: ', [player.name for player in table.handPlays[-1].players])
    input('waiting for key...')
    
def playLog(parameter_list):
    pass