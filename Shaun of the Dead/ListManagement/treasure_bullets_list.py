import turtle

class TreasureBulletsList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager, level_key):
        self.gameStartManager = gameStartManager
        self.treasure_bullets_list = self.gameStartManager.get("Treasure_Bullets", level_key)
        x=7

