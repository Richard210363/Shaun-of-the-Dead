import turtle
import Entities.enemy as enemy
import DataManagement.game_state_manager as game_state_manager

class EnemyList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager, level_key):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.enemies = self.gameStartManager.get("Enemies", level_key)  #Gets Value
        self.enemies_list = []

    def create_enemies_list(self):
        for position in range(3):
            zombie=self.enemies[position]
            self.enemies_list.append(enemy.Enemy(zombie["x_cor"], zombie["y_cor"], zombie["type"], zombie["name"], zombie["lives"], self.gameStateManager, self))

    def remove_enemy_from_list(self, enemy):
        self.enemies_list.remove(enemy)
        x=9

