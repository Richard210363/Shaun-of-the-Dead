import DataManagement.game_start_manager as game_start_manager_
import DataManagement.game_state_manager as game_state_manager_
import Main.shaun_of_the_dead as main_game_
import DataManagement.initialise_new_game as initialise_new_game_
import ListManagement.enemy_animation_list as enemy_animation_list_
import SOTD_DataManagement.data_manager as db_manager

#attributes = db_manager.get_player_attributes()

gameStartManager=game_start_manager_.GameStartManager("./ShaunOfTheDeadStartConditions.db")
#gameStartManager=game_start_manager_.GameStartManager("./ShaunOfTheDeadStartConditionsNPCandShaunexample.db")
gameStateManager=game_state_manager_.GameStateManager("./ShaunOfTheDeadGameState.db")
game=main_game_.ShaunOfTheDead(gameStateManager)
b=enemy_animation_list_.enemy_animation_list()
b.value = 5
c=enemy_animation_list_.enemy_animation_list()
x = c.value
print("Enter N for a new game")
print("Enter C to continue")
print("Enter a number to replay that level: 1 or 2")
user_input = input()
if user_input.upper() == "N":
    new_game = initialise_new_game_.initialise_new_game(gameStartManager, gameStateManager)
    new_game.initialise_level_one()
game.start(user_input)

