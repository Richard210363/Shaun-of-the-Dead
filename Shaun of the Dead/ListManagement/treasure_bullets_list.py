import turtle

class TreasureBulletsList(object):
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.treasure_bullets_list = []

    def fill_treasure_bullets_list(self):
        self.treasure_bullets_list = self.gameStateManager.get("Treasure_Bullets")

