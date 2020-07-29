import turtle

class TreasureLivesList(object):
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.treasure_lives_list = []

    def fill_treasure_lives_list(self):
        self.treasure_lives_list = self.gameStateManager.get("Treasure_Lives")


