#import Main.shaun_of_the_dead_23 as main_game

class register_new_user(object):
    """description of class"""

    new_user = input("Please enter your name:  ")
    print("")
    print("")
    print("Hi " + new_user)
    print("Enter S to start")
    print("Enter Q to quit")

    user_input = input()

    if user_input.upper()== "S":
    #    game=main_game.ShaunOfTheDead()
    #    game.start()
        x=5