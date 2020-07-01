class TestDatabase(object):
    """description of class"""


import DataManagement.game_state_manager as game_state_manager

gameStateManager = game_state_manager.GameStateManager("./ShaunOfTheDeadGameState.db")

gameStateManager.set("name" , "Holiday") #Sets Value
name = gameStateManager.get("name")  #Gets Value

x=5 # What does this do?