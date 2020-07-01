class ShaunOfTheDead(object):
    """description of class"""

import turtle
import math
import pygame

import Entities.enemy as enemy_
import Entities.player as player_
import Entities.treasure as treasure_
import Entities.bullet as bullet_
import Entities.wall_block as wall_block_
import ResourceManagement.sound_effects as sound_effect_
import DataManagement.game_state_manager as game_state_manager_
import ListManagement.enemy_list as enemy_list_

#Initialize the GameStateManager
gameStateManager = game_state_manager_.GameStateManager("./ShaunOfTheDeadGameState.db")  #new

#Prepare assets
turtle.register_shape("Zombie.gif")
turtle.register_shape("Left_Facing_Zombie.gif")
turtle.register_shape("Right_Facing_Zombie.gif")
turtle.register_shape("Shaun.gif")
turtle.register_shape("Left_Facing_Shaun.gif")
turtle.register_shape("Right_Facing_Shaun.gif")
turtle.register_shape("Wall.gif")
turtle.register_shape("Gun.gif")

#Define the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead v23")
wn.setup(700,700)

#Create items from classes
wallBlock = wall_block_.WallBlock()
player = player_.Player(gameStateManager)
treasure_bullets = treasure_.Treasure_Bullets()
treasure_lives = treasure_.Treasure_Lives()
enemy_list = enemy_list_.EnemyList()

#Create Lists
enemies = enemy_list.create_enemies_list()
walls = []
bullets = []

#Define what to do when we fire a bullet
def fire_bullet():
    if player.bullets > 0:
        player.bullets -= 1
        #Save Bullt state
        gameStateManager.set("bullets" , player.bullets) #new
        print ("Shaun has " + str(player.bullets) + " bullets remaining")
        current_bullet = bullet_.Bullet(player,walls)
        bullets.append(current_bullet)
        current_bullet.set_direction()
        sound_effect_.bulletSound.play()
    if player.bullets == 0:
        print ("Shaun has no bullets")

def moveEnemies():
    for enemy in enemies:
        enemy.move(player,walls)

def movebullets():
    for bullet in bullets:
        bullet.move()
      
#Define Level 1
level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX          XXXXX",
            "X  XXXXXXX  XXXXXX  XXXXX",
            "X  P  T XX  XXXXXX  XXXXX",
            "X    L  XX  XXX        XX",
            "XXXXXX  XX  XXX E      XX",
            "XXXXXX  XX  XXXXXX  XXXXX",
            "XXXXXX  XX    XXXX  XXXXX",
            "X  XXX        XXXX  XXXXX",
            "X  XXX  XXXXXXXXXXXXXXXXX",
            "X         XXXXXXXXXXXXXXX",
            "X          E      XXXXXXXX",
            "XXXXXXXXXXXX     XXXXX  X",
            "XXXXXXXXXXXXXXX  XXXXX  X",
            "XXX  XXXXXXXXXX         X",
            "XXX            E         X",
            "XXX         XXXXXXXXXXXXX",
            "XXXXXXXXXX  XXXXXXXXXXXXX",
            "XXXXXXXXXX              X",
            "XX   XXXXX              X",
            "XX   XXXXXXXXXXXXX  XXXXX",
            "XX    XXXXXXXXXXXX  XXXXX",
            "XX           XXXX       X",
            "XXXX                    X",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
           ]


#Define creating a level
def setup_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                wallBlock.goto(screen_x, screen_y)
                wallBlock.stamp()
                walls.append((screen_x,screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasure_bullets.goto(screen_x, screen_y)

            #if character == 'E':
            #    enemies.append(enemy.Enemy(screen_x, screen_y,gameStateManager))

            if character == "L":
                treasure_lives.goto(screen_x, screen_y)
           

#Everything above line this is preparing objects
###############################
#Everything below line this is the program that does things

player.walls = walls

#Create level and start game
setup_level(level_1)

#Listen to keyboard input
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,'d')
turtle.onkey(player.go_up,'w')
turtle.onkey(player.go_down,'s')
turtle.onkey(fire_bullet,'f')
wn.tracer(0)

# Main game loop
while True:

    for enemy in enemies:
        if enemy.is_collision_with_player(player):
            player.lives -=1
            if player.lives <= 0:
                print ("Shaun is DEAD!!")
            else:
                print ("Shaun has lost a life!!")
                print ("Shaun has got " + str(player.lives) + " lives remaining")

        for existing_bullet in bullets:
            if existing_bullet.is_collision(enemy):
                existing_bullet.destroy()
                enemy.wound()

    if player.is_collision_with_treasure_bullets(treasure_bullets):
        player.bullets += treasure_bullets.GetBullets("UnLimited")
        #Save player.bullets state
        gameStateManager.set("bullets" , player.bullets) #new
        print ("Shaun has " + str(player.bullets) + " bullets")

    if player.is_collision_with_treasure_lives(treasure_lives):
        player.lives += treasure_lives.lives
        #Save player.lives state
        gameStateManager.set("lives" , player.lives) #new
        print ("Shaun has gained a life")
        print ("Shaun has " + str(player.lives) + " lives")

    moveEnemies()
    movebullets()
    wn.update()
