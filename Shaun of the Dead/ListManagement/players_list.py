import turtle

class PlayersList(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager, level_key):
        self.gameStartManager = gameStartManager
        self.players_list = self.gameStartManager.get("Players", level_key)
        x=7


