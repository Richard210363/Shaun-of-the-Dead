import SOTD_DataManagement.data_manager as db_manager

class initialise_new_game(object):
    """description of class"""
    def __init__(self, gameStartManager, gameStateManager):
        self.gameStartManager = gameStartManager
        self.gameStateManager = gameStateManager
        self.new_game = ""

    def initialise_level_one(self):
        db_manager.initialise_current_database(1)
        self.new_game = self.gameStartManager.get_level("1")
        self.gameStateManager.memoryVersionOfDatabase = self.new_game
        self.gameStateManager.saveMemoryVersionOfDatabaseToFile()




