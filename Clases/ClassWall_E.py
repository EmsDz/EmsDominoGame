
#

from .ClassPlayer import player
from random import choice


class wall_E(player):
    """docstring for wall_E"""

    def __init__(self, name):
        player.__init__(self, name)
        self.imAbot = True
        self.tokensToPlay = []

    def autoPlay(self, table, handPlay):
        print(self.name +' : '+ 'has played: ')
        # if not table.tokens and handPlay.handPlayNumber == 1:
        if not table.tokens and self.name == handPlay.firstsTurn:
            table.addToken(self.tokens.pop('66'))
        elif not table.tokens:
            token = choice(self.tokens.keys())
            table.addToken(self.tokens.pop(token))

        self.makeTokensToPlay(table)
        token = choice(self.tokensToPlay).number

        if table.addToken(self.tokens[token]):
            self.tokens.pop(token)
            self.state = 'played'
        else:
            self.tokens[token].changeOrientation()
            table.addToken(self.tokens[token])
            self.tokens.pop(token)
            self.state = 'played'
        # else:
        #     self.passTurn()

    def makeTokensToPlay(self, table):
        self.tokensToPlay = []
        side = table.tokens[0].number[0] + table.tokens[-1].number[1]
        for playerTile in self.tokens:
            if side[0] in playerTile or side[1] in playerTile:
                try:
                    self.tokensToPlay.append(self.tokens[playerTile])
                except Exception:
                    self.tokensToPlay.append(self.tokens[playerTile[::-1]])
