class FencesList:
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.fences_list = []

    def fill_fences_list(self):
        self.fences_list = self.gameStateManager.get("Fences")
        pass
