class WallBlockList:
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.walls_list = []

    def fill_wall_list(self):
        self.walls_list = self.gameStateManager.get("Walls")
        pass
