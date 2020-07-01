class TestDatabase(object):
    """description of class"""

import turtle
import Entities.enemy as enemy
import DataManagement.game_state_manager as game_state_manager

turtle.register_shape("Zombie.gif")

#Initialize the GameStateManager
gameStateManager = game_state_manager.GameStateManager("./ShaunOfTheDeadStartConditions.db")  #new

enemies = gameStateManager.get("enemies")  #Gets Value


enemies_list = []

for position in range(3):
    zombie=enemies[position]
    enemies_list.append(enemy.Enemy(zombie["x_cor"], zombie["y_cor"], zombie["type"], zombie["name"], zombie["lives"], gameStateManager))
  
    
    x1=12





x=5 # What does this do?