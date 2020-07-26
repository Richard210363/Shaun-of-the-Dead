import DataManagement.game_start_manager as game_start_manager

class initialise_new_game(object):
    """description of class"""
    def __init__(self, gameStartManager):
        self.gameStartManager = gameStartManager

    def initialise_level_one(self):
        self.new_game = self.gameStartManager.get_level("1")
        pass




