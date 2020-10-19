class SafeAreaList:
    """description of class"""
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager
        self.safe_area_list = []

    def fill_safe_area_list(self):
        self.safe_area_list = self.gameStateManager.get("Safe_Area")
