
#


class handPlay(object):  # partida
    """docstring for handPlay"""

    def __init__(self, players):
        # super(handPlay, self).__init__()
        self.handPlayNumber = 0  # present handplay, is integer
        self.players = players  # players in this round, is a list
        self.firstsTurn = ''  # who play first
        self.winner = None  # name of the winner
        self.points = 0  # count of points of the current handPlay
        # self.passCount = 0
        self.currentRound = []
        self.handPlayLog = {}

    # make the order of play, that can vary in handplay to handplay
    def makePlayOrder(self):
        for t in range(0, len(self.players)):
            if self.players[t].name == self.firstsTurn:
                self.players = self.players[t:] + self.players[0:t]

    # finds the first turn in each start game
    def makeFirstsTurn(self):  # change to recibe an argument, player to check previous handPlay
        for x in ['66', '55', '44', '33', '22', '11', '00']:
            for player in self.players:
                if x in player.tokens:
                    self.firstsTurn = player.name
                    return
            # include player max token

    def openDoubleSix(self):  # add automatically the token
        # change name to be global
        if self.players[0].imAbot:
            # print(['[' + token[0] + '|' + token[1] + ']' for token in self.players[0].tokens])
            if '66' in self.players[0].tokens:
                print(self.players[0].name + ' Played: 66')
                return self.players[0].tokens.pop('66')
            token = 0
            for x in self.players[0].tokens:
                if int(x) > token:
                    token = int(x)
            print(self.players[0].name + 'Played: ' + str(token))
            return self.players[0].tokens.pop(str(token))

        else:  # modify to open with another token
            print('Open Double Six')
            print(self.players[0].name, 'Start This Round.')
            input('press enter to continue')
            print(['[' + token[0] + '|' + token[1] + ']' for token in self.players[0].tokens])
            x = input('Enter Token To Play: ')

            while x != '66' and '66' in self.players[0].tokens:  # little changed
                print('You Need To Start With 66.')
                x = input('Enter Token To Play: ')

            while x not in self.players[0].tokens:
                print('Invalid Token.')
                x = input('Enter Token Again: ')

            print(self.players[0].name + ' Played: ' + x)
            return self.players[0].tokens.pop(x)

    def checkWinner(self, player, table):  # can be eliminated
        if not player.tokens:
            self.winner = player.name
            self.points = table.countPoints()
            player.playerPoints += self.points
            # ??? make new handPlay ???
            # change players states
            return True
        return False
