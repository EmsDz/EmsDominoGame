

class game(object, table):  # debe eredar de mesa
    """docstring for game"""

    def __init__(self, points):
        super(game, self).__init__()
        self.handplays = []
        self.maxPuntuation = points


class player(object):
    """docstring for player"""

    def __init__(self, name, turn, partner):
        super(player, self).__init__()
        self.name = name  # player name, is a string
        self.tokens = {}  # player tokens, is a dictionary not a list
        self.turn = turn  # player turn, is a integer
        self.playerPoints = 0  # player points, is a integer
        self.partner = partner  # the partner of the player, is a string

    def addTokenToTable(self, token, table):
        if int(token) >= 0 and int(token) <= 66:
            if token in self.tokens or token[::-1] in self.tokens:
                table.addToken(token)

    def checkPlay(self, table):
        side = table.tokens[0][0] + table.tokens[len(table.tokens) - 1][1]
        for t in range(0, 2):
            for playerTile in self.tokens:
                if side[t] == playerTile.number[0] or side[t] == playerTile.number[1]:
                    return True
        return False

    def tokenPoints(self):
        points = 0
        for token in self.tokens:
            points += token.tokenValue()
        return points


class token(object):
    """docstring for token"""

    def __init__(self, num):
        super(token, self).__init__()
        self.number = num  # which number is in the token, is a string

    def changeOrientation(self):
        self.number = self.number[1] + self.number[0]

    def showToken(self):
        print(self.number)

    def tokenValue(self):
        return int(self.number[0]) + int(self.number[1])


class table(object):
    """docstring for table"""

    def __init__(self, tokens):
        super(table, self).__init__()
        self.tokens = tokens  # tokens that were played, is a list

    def countPoints(self):
        totalPoints = 168
        for token in self.tokens:
            totalPoints -= token.tokenValue()
        return totalPoints

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

    def clearTable(self):
        self.tokens = []

    def shuffleTokens(self, tokenList):
        random.shuffle(tokenList)

    def giveTokens(self, tokenList, playerList):
        for player in playerList:
            for t in range(0, 7):
                player.tokens[tokenList[0].number] = tokenList[0]
                tokenList.pop(0)


class handPlay(object):  # partida
    """docstring for handPlay"""

    def __init__(self, players, handPlayNumber, points):
        super(handPlay, self).__init__()
        self.players = players  # players in this round, is a list
        self.firtsTurn = ''  # who play first
        self.handPlayNumber = handPlayNumber  # present handplay, is integer
        self.winner = ''  # name of the winner
        self.points = points  # count of points of the current handPlay

    def makePlayOrder(self):
        for t in range(0, len(self.players)):
            if self.players[t].name == self.firtsTurn:
                return self.players[t:] + self.players[0:t]

    def makeFirstTurn(self):
        for player in self.players:
            for x in ['66', '55', '44', '33', '22', '11', '00']:
                if x in player.tokens:
                    self.firtsTurn = player.name
                    break
            # include player max token


class gameRules(object):
    """docstring for gameRules"""

    def __init__(self):
        super(gameRules, self).__init__()
