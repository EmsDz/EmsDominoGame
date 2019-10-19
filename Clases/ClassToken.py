
# this class is the principal of the game, is the token


class token(object):
    """docstring for token"""

    def __init__(self, num):
        self.number = num  # which number is in the token, is a string

    def changeOrientation(self):
        self.number = self.number[1] + self.number[0]

    def showToken(self):
        print('[' + self.number[0] + '|' + self.number[1] + ']', end='')

    def tokenValue(self):
        return int(self.number[0]) + int(self.number[1])
