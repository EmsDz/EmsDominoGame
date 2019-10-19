
#


class handPlay(object):  # partida
    """docstring for handPlay"""

    def __init__(self, players):
        self.handPlayNumber = 0  # present hand play, is integer
        self.players = players  # players in this round, is a list
        self.firstsTurn = ''  # who play first
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
        for x in ['66', '55', '44', '33', '22', '11', '00']:
            for player in self.players:
                if x in player.tokens:
                    self.firstsTurn = player.name
                    return
            # include player max token

    def openHandPlay(self, player):
        if player.imAbot:

            # play 66 automatically
            if '66' in player.tokens:
                print(player.name + ' Played: 66')
                return player.tokens.pop('66')

            token = 0
            for x in player.tokens:
                if int(x) > token:
                    token = int(x)
            print(player.name + ' Played: ' + str(token))
            return player.tokens.pop(str(token))

        # human play
        print('Open Double Six')
        print(player.name, 'Start This Round.')
        input('Press enter to continue')
        print(['[' + token[0] + '|' + token[1] + ']' for token in player.tokens])
        token = input('Enter Token To Play: ')

        while token not in player.tokens:  # controls the input
            if token != '66' and '66' in player.tokens:
                print('You Need To Start With 66.')
            else:
                print('Invalid Token.')
            token = input('Enter Token Again: ')

        print(player.name + ' Played: ' + token)
        return player.tokens.pop(token)
