import turtle

class WallBlockList(object):
    """description of class"""
    def __init__(self, gameStartManager, level_key):
        self.gameStartManager = gameStartManager
        self.walls_list = self.gameStartManager.get("Walls", level_key)
        x=7



