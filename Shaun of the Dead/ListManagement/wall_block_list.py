import turtle

class WallBlockList(object):
    """description of class"""
    def __init__(self, gameStartManager):
        self.gameStartManager = gameStartManager

    def fill_wall_list(self, level_key):
        self.walls_list = self.gameStartManager.get("Walls", level_key)


