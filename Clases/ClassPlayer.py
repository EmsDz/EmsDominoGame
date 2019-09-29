
# this class contend all the actions that can be do by the player


class player(object):
    """docstring for player"""

    def __init__(self, name):
        # super(player, self).__init__()
        self.name = name  # player name, is a string
        self.tokens = {}  # player tokens, is a dictionary not a list
        self.turn = 0  # player turn, is a integer
        self.satate = 'initial'  # player, "turn", status in each round [initial, played, passed]
        self.playerPoints = 0  # player points, is a integer
        self.partner = None  # the partner of the player, is a string

    # add a token to the variable tokens in table, sent it to be verified
    def addTokenToTable(self, token, table):
        if int(token) >= 0 and int(token) <= 66:
            if token in self.tokens or token[::-1] in self.tokens:
                table.addToken(token)

    # check if the player can play a token
    def checkPlay(self, table):
        side = table.tokens[0][0] + table.tokens[len(table.tokens) - 1][1]
        for t in range(0, 2):
            for playerTile in self.tokens:
                if side[t] == playerTile.number[0] or side[t] == playerTile.number[1]:
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
                self.tokens.append(table.tokenPit.pop(0))
            else:
                print("the tokenPit is empty")
        else:
            print("you have tokens to play")
