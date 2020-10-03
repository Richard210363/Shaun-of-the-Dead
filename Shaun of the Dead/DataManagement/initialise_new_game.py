import DataManagement.game_state_manager as game_state_manager_

class initialise_new_game(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.new_game

    def initialise_level_one(self):
        self.new_game = self.gameStartManager.get_level("1")
        self.gameStateManager.memoryVersionOfDatabase = self.new_game
        self.gameStateManager.saveMemoryVersionOfDatabaseToFile()
        pass




