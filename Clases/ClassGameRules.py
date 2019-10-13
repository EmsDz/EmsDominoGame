
# This class contents the basic rules of the game that can be applied


class gameRules(object):
    """docstring for gameRules"""

    def __init__(self):
        # super(gameRules, self).__init__()
        self.maxPuntuation = 50
        self.passAllPlayersPoints = 25
        self.keyTokenWinpoints = 50
        self.passCount = [0]

    def handPlayBlocked(self, player1):  # tomar en cuenta el num de jugadores ???
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

    def winHandPlay(self, player):  # can be better, count points, check if the points passed the maxPuntuation
        self.handPlays[-1].winner = player.name
        self.handPlays[-1].points = self.countPoints()

    def passAllPlayers(self):
        pass

    def endOfGame(self, players):  # can be changed
        if players[0].partner is not None:
            group1 = [players[0], players[2], players[0].playerPoints + players[2].playerPoints]
            group2 = [players[1], players[3], players[1].playerPoints + players[3].playerPoints]
            if group1[2] >= self.maxPuntuation:
                return group1[:2]
            elif group2[2] >= self.maxPuntuation:
                return [True, group2[:2]]
            return [False, '']

        for player in players:
            if player.playerPoints >= self.maxPuntuation:
                return [True, player]
        return [False, '']

    def keytokenWin(self):
        pass
