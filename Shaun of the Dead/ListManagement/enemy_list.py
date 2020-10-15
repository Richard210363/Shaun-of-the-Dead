import Entities.enemy as enemy_

class EnemyList(object):
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.enemies_list = []

    def fill_enemy_list(self):
        enemies = self.gameStateManager.get("Enemies") 
        for position in range(len(enemies)):
            single_enemy=enemies[position]
            self.enemies_list.append(enemy_.Enemy(single_enemy["x_cor"], single_enemy["y_cor"], single_enemy["type"], single_enemy["name"], single_enemy["lives"], self.gameStateManager, self))

    def remove_enemy_from_list(self, enemy):
        self.enemies_list.remove(enemy)