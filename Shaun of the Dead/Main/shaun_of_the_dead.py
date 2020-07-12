import turtle
import math
import pygame

import Entities.enemy as enemy_
import Entities.player as game_player_  #why did i call it this?
import Entities.treasure as treasure_
import Entities.bullet as bullet_
import Entities.wall_block as wall_block_
import ResourceManagement.sound_effects as sound_effect_
import DataManagement.game_state_manager as game_state_manager_
import DataManagement.game_start_manager as game_start_manager_
import ListManagement.enemy_list as enemy_list_
import ListManagement.wall_block_list as wall_block_list_

#SOTD
#This is from Richard

class ShaunOfTheDead(object):
    """description of class"""

    def __init__(self, gameStartManager, gameStateManager):
        #Initialize the GameStateManager
        self.gameStateManager = gameStateManager
        self.gameStartManager = gameStartManager

        self.quit=False

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
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Shaun of the Dead v23")
        self.wn.setup(700,700)

        #Create items from classes
        self.wallBlock = wall_block_.WallBlock()
        self.player = game_player_.Player(self.gameStateManager)
        self.treasure_bullets = treasure_.Treasure_Bullets()
        self.treasure_lives = treasure_.Treasure_Lives()
        self.level_key = self.gameStateManager.get("Current_Level")
        self.enemy_list = enemy_list_.EnemyList(self.gameStartManager, self.gameStateManager, self.level_key)
        self.wall_block_list = wall_block_list_.WallBlockList(self.gameStartManager, self.level_key)

        #Create Lists
        self.enemy_list.create_enemies_list()
        self.walls = []
        self.bullets = []

        self.player.walls = self.walls


        #Define Level 1
        self.level_1 = [
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
                    "X          E     XXXXXXXX",
                    "XXXXXXXXXXXX     XXXXX  X",
                    "XXXXXXXXXXXXXXX  XXXXX  X",
                    "XXX  XXXXXXXXXX         X",
                    "XXX            E        X",
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


    #Define what to do when we fire a bullet
    def fire_bullet(self):
        if self.player.bullets > 0:
            self.player.bullets -= 1
            #Save Bullt state
            self.gameStateManager.set("bullets" , self.player.bullets) #new
            print ("Shaun has " + str(self.player.bullets) + " bullets remaining")
            current_bullet = bullet_.Bullet(self.player,self.walls)
            self.bullets.append(current_bullet)
            current_bullet.set_direction()
            sound_effect_.bulletSound.play()
        if self.player.bullets == 0:
            print ("Shaun has no bullets")

    def moveEnemies(self):
        for enemy in self.enemy_list.enemies_list:
            enemy.move(self.player,self.walls)

    def drawsWalls(self):
        for wall in self.wall_block_list.walls_list:
            screen_x=wall[0]
            screen_y=wall[1]
            self.wallBlock.goto(screen_x, screen_y)
            self.wallBlock.stamp()
            self.walls.append((screen_x,screen_y))

    def quit_game(self):
        self.quit = True

    def movebullets(self):
        for bullet in self.bullets:
            bullet.move()
      
    #Define creating a level
    def setup_level(self, level):
        self.drawsWalls()
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]

                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "P":
                    self.player.goto(screen_x, screen_y)

                if character == "T":
                    self.treasure_bullets.goto(screen_x, screen_y)

                if character == "L":
                    self.treasure_lives.goto(screen_x, screen_y)
           

#Everything above line this is preparing objects
###############################
#Everything below line this is the program that does things


    def start(self):
        
        #Create level
        self.setup_level(self.level_1)

        #Listen to keyboard input
        turtle.listen()
        turtle.onkey(self.player.go_left,"a")
        turtle.onkey(self.player.go_right,'d')
        turtle.onkey(self.player.go_up,'w')
        turtle.onkey(self.player.go_down,'s')
        turtle.onkey(self.fire_bullet,'f')
        turtle.onkey(self.quit_game,'q')
        self.wn.tracer(0)

        # Main game loop
        while not self.quit:

            for enemy in self.enemy_list.enemies_list:
                if enemy.is_collision_with_player(self.player):
                    self.player.lives -=1
                    if self.player.lives <= 0:
                        print ("Shaun is DEAD!!")
                    else:
                        print ("Shaun has lost a life!!")
                        print ("Shaun has got " + str(self.player.lives) + " lives remaining")

                for bullet in self.bullets:
                    if bullet.is_collision(enemy):
                        bullet.destroy()
                        enemy.wound()

            if self.player.is_collision_with_treasure_bullets(self.treasure_bullets):
                self.player.bullets += self.treasure_bullets.GetBullets("UnLimited")
                #Save player.bullets state
                self.gameStateManager.set("bullets" , self.player.bullets) #new
                print ("Shaun has " + str(self.player.bullets) + " bullets")

            if self.player.is_collision_with_treasure_lives(self.treasure_lives):
                self.player.lives += self.treasure_lives.lives
                #Save player.lives state
                self.gameStateManager.set("lives" , self.player.lives) #new
                print ("Shaun has gained a life")
                print ("Shaun has " + str(self.player.lives) + " lives")

            self.moveEnemies()
            self.movebullets()
            self.wn.update()

        self.wn.bye()
            

    
    
