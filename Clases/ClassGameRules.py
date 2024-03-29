
# This class contents the basic rules of the game that can be applied


class gameRules(object):
    """docstring for gameRules"""

    def __init__(self, maxPunt=150):
        self.maxPuntuation = maxPunt
        self.passAllPlayersPoints = 25
        self.keyTokenWinpoints = 50
        self.passCount = [0]

    def handIsBlocked(self):
        if self.passCount[0] == len(self.handPlays[-1].players):
            return True
        return False

    def validateToken(self, token, player):
        if token not in player.tokens and token[::-1] not in player.tokens:
            return True
        if len(token) > 2 or len(token) < 2:
            return True
        if token[0] not in ['0', '1', '2', '3', "4", '5', '6'] or token[1] not in ['0', '1', '2', '3', "4", '5', '6']:
            return True
        return False

    def blockedWin(self, player1):
        i = self.handPlays[-1].players.index(player1) + 1
        if i == len(self.handPlays[-1].players):
            player2 = self.handPlays[-1].players[0]
        else:
            player2 = self.handPlays[-1].players[i]

        print('\n', player1.name, ' Blocked the hand.\n')
        print(player1.name + ':', str(player1.tokenPoints()) + '  vs  ', end='')
        print(player2.name + ':', str(player2.tokenPoints()))
        print('\n')

        if player1.tokenPoints() <= player2.tokenPoints():
            self.normalWin(player1)
        else:
            self.normalWin(player2)

    def normalWin(self, player):  # can be better
        self.handPlays[-1].winner = player.name
        self.handPlays[-1].points = self.countPoints()
        player.playerPoints += self.handPlays[-1].points
        print('\n#### End Of the Hand ####')

        if not self.handIsBlocked():
            self.keytokenWin(player)

        self.passCount = [0]
        self.tokens = []
        self.clearPlayerTokens(self.handPlays[-1].players)
        print('##The Winner is: ', player.name, end='\n')

    def passOtherPlayers(self, player):
        print('\nYou pass all other players so you win ', self.passAllPlayersPoints, ' points for that.\n')
        player.playerPoints += self.passAllPlayersPoints

    def endOfGame(self, players):  # can be changed
        if players[0].partner is not None:
            group1 = [players[0].name, players[2].name, players[0].playerPoints + players[2].playerPoints]
            group2 = [players[1].name, players[3].name, players[1].playerPoints + players[3].playerPoints]
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
                return [True, player.name]
        return [False, '']

    # "k píkua"
    def keytokenWin(self, player):
        lastToken = self.lastState[2].number
        tableSides = self.lastState[1]
        if lastToken == tableSides or lastToken[::-1] == tableSides:
            print('\n', player.name, ' Win by k Pikua!!! and win ', self.keyTokenWinpoints, ' Points.\n')
            player.playerPoints += self.keyTokenWinpoints
