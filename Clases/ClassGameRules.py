
# This class contents the basic rules of the game that can be applied


class gameRules(object):
    """docstring for gameRules"""

    def __init__(self):
        # super(gameRules, self).__init__()
        self.maxPuntuation = 50
        self.passAllPlayersPoints = 25
        self.keyTokenWinpoints = 50
        self.passCount = [0]

    def handPlayBlocked(self, player1):
        if self.passCount[0] == 4:
            i = self.handPlays[-1].players.index(player1) + 1
            if i == 4:
                player2 = self.handPlays[-1].players[0]
            else:
                player2 = self.handPlays[-1].players[i]
                
            if player1.tokenPoints >= player2.tokenPoints:
                self.winHandPlay(player1)
            else:
                self.winHandPlay(player2)

    def winHandPlay(self, player):
        self.handPlays[-1].winner = player.name
        self.handPlays[-1].points = self.countPoints()

    def passAllPlayers(self):
        pass
    
    def endOfGame(self, players):
        if players[0].partner != None:
            pass
        
        for player in players:
            if player.playerPoints >= self.maxPuntuation:
                return [True, player]
        return [False, '']

