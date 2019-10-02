
class handPlay(object):  # partida
    """docstring for handPlay"""

    def __init__(self, players):
        # super(handPlay, self).__init__()
        self.handPlayNumber = 0  # present handplay, is integer
        self.players = players  # players in this round, is a list
        self.firstsTurn = ''  # who play first
        self.winner = None  # name of the winner
        self.points = 0  # count of points of the current handPlay
        self.passCount = 0
        # self.currentRound = None
        # self.handplayLog = None

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

    def openDoubleSix(self, players):
        pass

    def checkWinner(self, player, table):
        if not player.tokens:
            self.winner = player.name
            self.points = table.countPoints()
            return True
        return False
