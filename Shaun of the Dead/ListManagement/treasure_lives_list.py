import turtle
import Entities.treasure as treasure

class TreasureLivesList(object):
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.treasure_lives_list = []

    def fill_treasure_lives_list(self):
        treasure_lives = self.gameStateManager.get("Treasure_Lives")
        for position in range(len(treasure_lives)):
            single_treasure_life=treasure_lives[position]
            self.treasure_lives_list.append(treasure.Treasure_Lives(single_treasure_life[0], single_treasure_life[1]))

