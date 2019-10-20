
#

from .ClassPlayer import player
from random import choice


class wall_E(player):
    """docstring for wall_E"""

    def __init__(self, name):
        player.__init__(self, name)
        self.imAbot = True
        self.tokensToPlay = []

    def autoPlay(self, table):
        self.makeTokensToPlay(table)
        token = choice(self.tokensToPlay)  # select a random token to play

        # add token to table, change orientation otherwise
        number = token.number  # to show the token right
        if not table.addToken(token):
            token.changeOrientation()
            number = token.number  # to show the token right
            table.addToken(token)

        self.state = 'played'
        print(self.name + ' has played: ' + number)
        table.handPlays[-1].currentRound.append([self, number])

        if number not in self.tokens:
            number = number[::-1]
        self.tokens.pop(number)
        return

    # create a list with the tokens that the bot can play
    def makeTokensToPlay(self, table):
        self.tokensToPlay = []
        side = table.tokens[0].number[0] + table.tokens[-1].number[1]
        for playerTile in self.tokens:
            if side[0] in playerTile or side[1] in playerTile:
                try:
                    self.tokensToPlay.append(self.tokens[playerTile])
                except Exception:
                    self.tokensToPlay.append(self.tokens[playerTile[::-1]])
