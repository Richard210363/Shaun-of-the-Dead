import turtle

class WallBlockList(object):
    """description of class"""
    def __init__(self, gameStartManager):
        self.gameStartManager = gameStartManager
        self.walls_list = self.gameStartManager.get("Level_01")


