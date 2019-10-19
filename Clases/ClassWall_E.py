
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
        token = choice(self.tokensToPlay).number  # select a ramdome token to play

        # little error fixed, -key index-
        if token not in self.tokens:
            token = token[1] + token[0]

        if table.addToken(self.tokens[token]):
            self.tokens.pop(token)
            self.state = 'played'
        else:
            self.tokens[token].changeOrientation()
            table.addToken(self.tokens[token])
            self.tokens.pop(token)
            self.state = 'played'
        print(self.name + ' has played: ' + token)
        return token

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
