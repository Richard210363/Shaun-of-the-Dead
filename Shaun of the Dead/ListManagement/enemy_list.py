import turtle
import Entities.enemy as enemy
import DataManagement.game_state_manager as game_state_manager

class EnemyList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.enemies_list = []

    def fill_enemy_list(self, level_key):
        enemies = self.gameStateManager.get("Enemies")
        for position in range(3):
            single_enemy=enemies[position]
            self.enemies_list.append(enemy.Enemy(single_enemy["x_cor"], single_enemy["y_cor"], single_enemy["type"], single_enemy["name"], single_enemy["lives"], self.gameStateManager, self))

    def remove_enemy_from_list(self, enemy):
        self.enemies_list.remove(enemy)
        x=9

