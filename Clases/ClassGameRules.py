
# This class contents the basic rules of the game that can be applied


class gameRules(object):
    """docstring for gameRules"""

    def __init__(self, maxPunt=50):
        self.maxPuntuation = maxPunt
        self.passAllPlayersPoints = 25
        self.keyTokenWinpoints = 50
        self.passCount = [0]

    def handIsBlocked(self):
        if self.passCount[0] == len(self.handPlays[-1].players):
            return True
        return False

    def blockedWin(self, player1):
        i = self.handPlays[-1].players.index(player1) + 1
        if i == len(self.handPlays[-1].players):
            player2 = self.handPlays[-1].players[0]
        else:
            player2 = self.handPlays[-1].players[i]

        if player1.tokenPoints() >= player2.tokenPoints():
            self.normalWin(player1)
        else:
            self.normalWin(player2)

    def normalWin(self, player):  # can be better
        self.handPlays[-1].winner = player.name
        self.handPlays[-1].points = self.countPoints()
        player.playerPoints += self.handPlays[-1].points
        print('End Of the Hand')

        if not self.handIsBlocked():
            self.keytokenWin(player)

        self.clearTable()
        self.passCount = 0
        self.clearPlayerTokens(self.handPlays[-1].players)
        print('The Winner is: ', player.name, end='\n')

    def passOtherPlayers(self):
        pass

    def endOfGame(self, players):  # can be changed
        if players[0].partner is not None:
            group1 = [players[0], players[2], players[0].playerPoints + players[2].playerPoints]
            group2 = [players[1], players[3], players[1].playerPoints + players[3].playerPoints]
            if group1[2] >= self.maxPuntuation:
                self.gameHasEnded = True
                return group1[:2]
            elif group2[2] >= self.maxPuntuation:
                self.gameHasEnded = True
                return [True, group2[:2]]
            return [False, '']

        for player in players:
            if player.playerPoints >= self.maxPuntuation:
                self.gameHasEnded = True
                # print('Points: ', player.playerPoints)
                return [True, player.name]
        return [False, '']

    # "k píkua"
    def keytokenWin(self, player):
        lastToken = self.lastState[2].number
        tableSides = self.lastState[1]
        if lastToken == tableSides or lastToken[::-1] == tableSides:
            print('\n', player.name, ' Win by k Pikua!!! and win ', self.keyTokenWinpoints, ' Points.\n')
            player.playerPoints += self.keyTokenWinpoints
