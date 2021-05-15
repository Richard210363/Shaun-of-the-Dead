import Entities.enemy as enemy_
import SOTD_DataManagement.data_manager as db_manager

class EnemyList(object):
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.enemies_list = []

    def fill_enemy_list(self):
        enemies = db_manager.get_current_enemy_attributes()
        for position in range(len(enemies)):
            single_enemy=enemies[position]
            self.enemies_list.append(enemy_.Enemy(single_enemy["x_coordinate"], single_enemy["y_coordinate"], single_enemy["type"], single_enemy["name"], single_enemy["lives"], self.gameStateManager, self))
            self.enemies_list[position].initialise()

    def remove_enemy_from_list(self, enemy):
        self.enemies_list.remove(enemy)