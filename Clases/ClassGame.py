
# this class is the principal of the game, it start the game

from ClassTable import table, shuffle
from ClassGameRules import gameRules
from ClassToken import token
from ClassPlayer import player


class game(table, gameRules):  # debe eredar de mesa
    """docstring for game"""

    def __init__(self):
        # super(game, self).__init__()
        self.handplays = []
        self.tokenBox = []

    def newHandPlay(self, handplay):
        self.handplays.append(handplay)
        self.handplays[-1].handNlayNumber = len(self.handplays)

    def makeTokenBox(self):
        for x in range(0, 7):
            for z in range(x, 7):
                self.tokenBox.append(token(str(x) + str(z)))
