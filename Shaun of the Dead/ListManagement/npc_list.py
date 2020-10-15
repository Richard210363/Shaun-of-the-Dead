import Entities.non_player_character as npc

class NPCList:
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.npc_list = []

    def fill_npc_list(self):
        npcs_from_database = self.gameStateManager.get("NPC")
        for position in range(1):
            single_npc=npcs_from_database[position]
            self.npc_list.append(npc.NPC(single_npc["x_cor"], single_npc["y_cor"], single_npc["bullets"], single_npc["name"], single_npc["lives"], self.gameStateManager))

 

