import turtle
import Entities.player as player

class PlayersList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.players_list = []

    def fill_player_list(self, level_key):
        players = self.gameStartManager.get("Players", level_key)
        for position in range(1):
            single_player=players[position]
            self.players_list.append(player.Player(single_player["x_cor"], single_player["y_cor"], single_player["bullets"], single_player["name"], single_player["lives"], self.gameStateManager, self))


 

