
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

        if table.validateToken(token, self):
            input('That token does not exits or you do not have it. Enter to continue.')
            return False

        try:
            value = table.addToken(self.tokens[token])
        except Exception:
            self.tokens[token[::-1]].changeOrientation()
            value = table.addToken(self.tokens[token[::-1]])

        if value:
            self.state = 'played'
        else:
            input('That token can not be put in the table!!, Enter to continue.')
        return value

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
            points += self.tokens[token].tokenValue()
        return points

    def getTokenFromTokenPit(self, table):
        if not self.checkPlay(table):
            if table.tokenPit:
                token = table.tokenPit.pop(0)
                self.tokens[token.number] = token
            else:
                print("The token Pit is Empty")
        else:
            print("You have tokens to play")

    def showPlayerTokens(self):
        print(self.name, ' Tokens: ', end='')
        print('[ ', end='')
        for token in self.tokens:
            self.tokens[token].showToken()
            print(' ', end='')
        print(']', end='')
        print()

    def leaveGame(self):
        while True:
            p = input('\n\nYou realy want to exit? YES/NO \nYour answer: ').upper()
            if p in ['N', 'NO']:
                return False
            if p in ['Y', 'YES']:
                return True
        # return
