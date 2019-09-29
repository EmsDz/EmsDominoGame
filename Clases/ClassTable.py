
# this class is the core of the game, ...

from random import shuffle


class table(object):
    """docstring for table"""

    def __init__(self):
        # super(table, self).__init__()
        self.tokens = []  # tokens that were played, is a list
        self.tokenPit = []  # contend the tokens that rest, that does not have player yet

    # return the sum of all tokens outside of the table
    def countPoints(self):
        totalPoints = 168
        for token in self.tokens:
            totalPoints -= token.tokenValue()
        return totalPoints

    # verifies the position of the token to put it in the table
    def addToken(self, token):  # getToken
        if self.tokens == []:
            self.tokens.append(token)
        elif token.number[0] == self.tokens[0].number[0]:
            token.changeOrientation()
            self.tokens = [token] + self.tokens
        else:
            if token.number[0] != self.tokens[len(self.tokens) - 1].number[1]:
                token.changeOrientation()
            self.tokens.append(token)

    # clean the tokens variable
    def clearTable(self):  # can be eliminate?
        self.tokens = []

    # clean the tokens of each player
    def clearPlayerTokens(self, playerList):
        for player in playerList:
            player.tokens = {}

    # put the  tokens randomly
    def shuffleTokens(self, tokenList):  # can be better?, respect to cleanTable()
        if len(self.tokens) < 28:
            self.clearTable()
            self.tokens += tokenList
        shuffle(self.tokens)

    # give 7 tokens for each player
    def giveTokens(self, playerList):
        for player in playerList:
            for t in range(0, 7):  # can be better, ...
                player.tokens[self.tokens[0].number] = self.tokens[0]
                self.tokens.pop(0)
        if self.tokens:
            self.tokenPit += self.tokens
            self.clearTable()

    def giveFromTokenpit(self, player):
        player.tokens.append(self.tokenPit.pop(0))

    def showTableTokens(self):
        for token in self.tokens:
            token.showToken()
        print()
