import turtle

class TreasureLivesList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager, level_key):
        self.gameStartManager = gameStartManager
        self.treasure_lives_list = self.gameStartManager.get("Treasure_Lives", level_key)
        x=7


