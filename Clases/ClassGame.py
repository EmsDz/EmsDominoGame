
# this class is the principal of the game, it start the game

from ClassTable import table, shuffle
# import ClassTable


class game(table):  # debe eredar de mesa
    """docstring for game"""

    def __init__(self, points):
        super(game, self).__init__()
        self.handplays = []
        self.maxPuntuation = points
