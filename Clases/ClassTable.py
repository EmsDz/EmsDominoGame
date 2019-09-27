
# this class is the core of the game, ...

from random import shuffle


class table(object):
    """docstring for table"""

    def __init__(self, tokens):
        super(table, self).__init__()
        self.tokens = tokens  # tokens that were played, is a list
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
    def clearTable(self):
        self.tokens = []

    # put the  tokens randomly
    def shuffleTokens(self, tokenList):
        shuffle(tokenList)

    # give 7 tokens for each player
    def giveTokens(self, tokenList, playerList):
        for player in playerList:
            for t in range(0, 7):  # can be better, ...
                player.tokens[tokenList[0].number] = tokenList[0]
                tokenList.pop(0)
        if tokenList:
            self.tokenPit += tokenList
            clearTable()

    def giveFromTokenpit(self):
        pass
