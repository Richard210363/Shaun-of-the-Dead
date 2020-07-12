import DataManagement.game_start_manager as game_start_manager_
import DataManagement.game_state_manager as game_state_manager_
import Main.shaun_of_the_dead as main_game_

gameStartManager=game_start_manager_.GameStartManager("./ShaunOfTheDeadStartConditions.db")
gameStateManager=game_state_manager_.GameStateManager("./ShaunOfTheDeadGameState.db")
game=main_game_.ShaunOfTheDead(gameStartManager, gameStateManager)
print("Enter R to restart")
print("Enter C to continue")
user_input = input()
game.start(user_input)

