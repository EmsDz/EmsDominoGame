
class handPlay(object):  # partida
    """docstring for handPlay"""

    def __init__(self, players):
        # super(handPlay, self).__init__()
        self.players = players  # players in this round, is a list
        self.firtsTurn = ''  # who play first
        self.handPlayNumber = 0  # present handplay, is integer
        self.winner = ''  # name of the winner
        self.points = 0  # count of points of the current handPlay
        # self.currentRound = None
        # self.handplayLog = None

    # make the order of play, that can vary in handplay to handplay
    def makePlayOrder(self):
        for t in range(0, len(self.players)):
            if self.players[t].name == self.firtsTurn:
                return self.players[t:] + self.players[0:t]

    # finds the first turn in each start game
    def makeFirstTurn(self):
        for player in self.players:
            for x in ['66', '55', '44', '33', '22', '11', '00']:
                if x in player.tokens:
                    self.firtsTurn = player.name
                    break
            # include player max token
