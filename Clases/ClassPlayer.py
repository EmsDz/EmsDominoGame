
# this class contend all the actions that can be do by the player


class player(object):
    """docstring for player"""

    def __init__(self, name):
        # super(player, self).__init__()
        self.name = name  # player name, is a string
        self.tokens = {}  # player tokens, is a dictionary not a list
        self.turn = 0  # player turn, is a integer
        self.state = 'initial'  # player, "turn", status in each round [initial, played, passed]
        self.playerPoints = 0  # player points, is a integer
        self.partner = None  # the partner of the player, is a string
        self.imAbot = False

    # add a token to the variable tokens in table, sent it to be verified
    def addTokenToTable(self, token, table):
        if len(token) != 2 or token[0] not in '0123456' or token[1] not in '0123456':
            return False

        if token in self.tokens or token[::-1] in self.tokens:
            try:
                if table.addToken(self.tokens[token]):
                    self.tokens.pop(token)
                    self.state = 'played'
                    return True
            except Exception:
                self.tokens[token[::-1]].changeOrientation()
                if table.addToken(self.tokens[token[::-1]]):
                    self.tokens.pop(token[::-1])
                    self.state = 'played'
                    return True
        return False

    def passTurn(self):
        self.state = 'passed'

    # check if the player can play a token
    def checkPlay(self, table):
        if not table.tokens:
            return True

        side = table.tokens[0].number[0] + table.tokens[-1].number[1]
        for t in range(0, 2):
            for playerTile in self.tokens:
                if side[t] == playerTile[0] or side[t] == playerTile[1]:
                    return True
        return False

    # return the points that have the player at the present moment
    def tokenPoints(self):
        points = 0
        for token in self.tokens:
            points += token.tokenValue()
        return points

    def getTokenFromTokenPit(self, table):
        if not self.checkPlay(table):
            if table.tokenPit:
                token = table.tokenPit.pop(0)
                self.tokens[token] = token
            else:
                print("the tokenPit is empty")
        else:
            print("you have tokens to play")
