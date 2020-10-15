import Entities.treasure as treasure

class TreasureBulletsList(object):
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.treasure_bullets_list = []

    def fill_treasure_bullets_list(self):
        treasure_bullets = self.gameStateManager.get("Treasure_Bullets")
        for position in range(len(treasure_bullets)):
            single_treasure_bullet=treasure_bullets[position]
            self.treasure_bullets_list.append(treasure.Treasure_Bullets(single_treasure_bullet[0], single_treasure_bullet[1]))     

