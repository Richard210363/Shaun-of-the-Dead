import turtle
import Entities.player as player

class NPCList:
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.npc_list = []

    def fill_npc_list(self, level_key):
        npcs_from_database = self.gameStartManager.get("Players", level_key)
        for position in range(2):
            single_npc=npcs_from_database[position]
            self.npc_list.append(player.Player(single_npc["x_cor"], single_npc["y_cor"], single_npc["bullets"], single_npc["name"], single_npc["lives"], self.gameStateManager, self))


 

