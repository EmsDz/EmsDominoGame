
# this class is the principal of the game, it start the game

from .ClassTable import table, shuffle
from .ClassGameRules import gameRules
from .ClassToken import token
from .ClassPlayer import player
from .ClassWall_E import wall_E


class game(table, gameRules):
    """docstring for game"""

    def __init__(self):
        table.__init__(self)
        gameRules.__init__(self)
        self.handPlays = []
        self.tokenBox = []
        self.playerList = []
        self.Bots = shuffle([wall_E('Bobby'), wall_E('Brayan'), wall_E('Teddy'), wall_E('Trebon')])
        self.gameHasEnded = False

    def newHandPlay(self, handplay):
        self.handPlays.append(handplay)
        self.handPlays[-1].handPlayNumber = len(self.handPlays)

    def makeTokenBox(self):
        for x in range(6, -1, -1):
            for z in range(x, -1, -1):
                self.tokenBox.append(token(str(x) + str(z)))

    def makeGroups(self):
        pass

    # make player?
