
#


class handPlay(object):  # partida
    """docstring for handPlay"""

    def __init__(self, players):
        self.handPlayNumber = 0  # present hand play, is integer
        self.players = players  # players in this round, is a list
        self.firstsTurn = ''  # who play first
        self.openGameToken = ''  # the token that start the game
        self.winner = None  # name of the winner
        self.points = 0  # count of points of the current handPlay
        self.currentRound = []
        self.handPlayLog = {}

    # make the order of play, that can vary in handplay to handplay
    def makePlayOrder(self):
        for t in range(0, len(self.players)):
            if self.players[t].name == self.firstsTurn:
                self.players = self.players[t:] + self.players[0:t]

    # finds the first turn in each start game
    def makeFirstsTurn(self):
        # look for a double
        for double in ['66', '55', '44', '33', '22', '11', '00']:
            # raise Exception('something happend')
            for player in self.players:
                if double in player.tokens:
                    self.firstsTurn = player.name
                    self.openGameToken = double
                    return
        # look for maximum token
        maxToken = 0
        for player in self.players:
            for x in player.tokens:
                if int(x) > maxToken:
                    temporaryFirstsTurn = player.name
                    maxToken = int(x)
        self.firstsTurn = temporaryFirstsTurn
        self.openGameToken = str(maxToken)
        return

    def openHandPlay(self, player):
        print('Open With Double')
        print(player.name, 'Start This Round.')
        input('Press enter to continue')

        if player.imAbot:
            # play automatically
            if self.openGameToken == '':
                maxToken = 0
                for x in player.tokens:
                    if int(x) > maxToken:
                        maxToken = int(x)
                self.openGameToken = str(maxToken)

            print(player.name + ' Played: ', self.openGameToken)
            return player.tokens.pop(self.openGameToken)

        # human play
        player.showPlayerTokens()
        token = input('Enter Token To Play: ').upper()

        # ended game
        if token in ['X', 'SALIR', 'EXIT', 'EX', 'CLOSE', 'END']:
            if player.leaveGame():
                return 'EXIT'

        # controls the input
        while token not in player.tokens or token != self.openGameToken:
            if token != self.openGameToken and self.openGameToken in player.tokens:
                if self.handPlayNumber != 1:
                    break
                print('You Need To Start With a Double. A bigger one, like: ', self.openGameToken)
            elif token not in player.tokens:
                print('Invalid Token.')
            else:
                break
            token = input('Enter Token Again: ')

        print(player.name + ' Played: ' + token)
        return player.tokens.pop(token)

    def showHandLog(self):
        for l in self.handPlayLog:
            print(str(l), end=' ')
            for log in self.handPlayLog[l]:
                print(log[0].name + ': ' + log[1], end=' ')
            print('')
        print('\n')
