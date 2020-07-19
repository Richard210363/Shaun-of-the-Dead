import turtle
import Entities.player as player

class PlayersList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager, level_key):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.players = self.gameStartManager.get("Players", level_key)
        self.players_list = []
        x=7

    def create_players_list(self):
        for position in range(1):
            players=self.players[position]
            self.players_list.append(player.Player(players["x_cor"], players["y_cor"], players["bullets"], players["name"], players["lives"], self.gameStateManager, self))

