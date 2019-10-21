
# this class is the principal of the game, it start the game

import os
from .ClassTable import table, shuffle
from .ClassGameRules import gameRules
from .ClassToken import token
# from .ClassPlayer import player
from .ClassWall_E import wall_E


class game(table, gameRules):
    """docstring for game"""

    def __init__(self):
        table.__init__(self)
        gameRules.__init__(self)
        self.handPlays = []
        self.tokenBox = []
        self.playerList = []
        self.Bots = [wall_E('Bobby'), wall_E('Brayan'), wall_E('Teddy'), wall_E('Trebon')]
        shuffle(self.Bots)
        self.gameHasEnded = False

    def newHandPlay(self, handplay):
        self.handPlays.append(handplay)
        self.handPlays[-1].handPlayNumber = len(self.handPlays)
        self.passCount = [0]
        self.tokens = []

    def makeTokenBox(self):
        for x in range(6, -1, -1):
            for z in range(x, -1, -1):
                self.tokenBox.append(token(str(x) + str(z)))

    # cls, borrar pantalla
    def Pycls(self):
        return os.system("cls")

    def makeGroups(self):
        pass

    def showGameStatus(self):
        print('\n')
        print('            ', end='')
        for player in self.handPlays[-1].players:
            print(player.name + ': ' + str(player.playerPoints), end='      ')
        print('')

    # make player?
