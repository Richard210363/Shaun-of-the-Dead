import turtle
import math
import pygame
import time

import Entities.enemy as enemy_
import Entities.player as game_player_
import Entities.treasure as treasure_
import Entities.bullet as bullet_
import Entities.wall_block as wall_block_
import Entities.non_player_character as non_player_character_
import ResourceManagement.sound_effects as sound_effect_
import DataManagement.game_state_manager as game_state_manager_
import ListManagement.enemy_list as enemy_list_
import ListManagement.wall_block_list as wall_block_list_
import ListManagement.npc_list as npc_list_
import ListManagement.treasure_lives_list as treasure_lives_list_
import ListManagement.treasure_bullets_list as treasure_bullets_list_
import ListManagement.fences_list as fences_list_

class ShaunOfTheDead:
    """description of class"""

    def __init__(self, gameStateManager):
        #Initialize the GameStateManager
        self.gameStateManager = gameStateManager

        self.quit=False

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
            enemy.move(self.player,self.walls,self.fences)

    def moveNPC(self):
        for npc in self.npc_list.npc_list:
            npc.move(self.walls, self.player, self.enemy_list.enemies_list, self.bullets)



    def drawsEnemies(self):
        for enemy in self.enemy_list.enemies_list:
            screen_x=enemy.x_cor
            screen_y=enemy.y_cor
            enemy.goto(screen_x, screen_y)

    def drawsWalls(self):
        for wall in self.wall_block_list.walls_list:
            screen_x=wall[0]
            screen_y=wall[1]
            self.wallBlock.goto(screen_x, screen_y)
            self.wallBlock.stamp()
            self.walls.append((screen_x,screen_y))

    def drawsNPC(self):
        for npc in self.npc_list.npc_list:
            screen_x=npc.x_cor
            screen_y=npc.y_cor
            npc.goto(screen_x, screen_y)

    def drawsTreasureLives(self):
        for treasure_life in self.treasure_lives_list.treasure_lives_list:
            screen_x=treasure_life.x_cor
            screen_y=treasure_life.y_cor
            treasure_life.goto(screen_x, screen_y)

    def drawsTreasureBullets(self):
        for treasure_bullet in self.treasure_bullets_list.treasure_bullets_list:
            screen_x=treasure_bullet.x_cor
            screen_y=treasure_bullet.y_cor
            treasure_bullet.goto(screen_x, screen_y)

    def drawsPlayer(self):
        screen_x=self.player.x_cor
        screen_y=self.player.y_cor
        self.player.goto(screen_x, screen_y)

    def fillFences(self):
        for fence in self.fences_list.fences_list:
            screen_x=fence[0]
            screen_y=fence[1]
            self.fences.append((screen_x,screen_y))

    def quit_game(self):
        self.quit = True

    def movebullets(self):
        for bullet in self.bullets:
            bullet.move()
      
    #Define creating a level
    def setup_level(self):
        self.drawsNPC()
        self.drawsEnemies()
        self.drawsWalls()
        self.drawsTreasureLives()
        self.drawsTreasureBullets()
        self.drawsPlayer()
        self.fillFences()
           
    def start(self, start_mode):
        #Prepare assets
        turtle.register_shape("Resources\\Zombie.gif")
        turtle.register_shape("Resources\\Left_Facing_Zombie.gif")
        turtle.register_shape("Resources\\Right_Facing_Zombie.gif")
        turtle.register_shape("Resources\\Shaun.gif")
        turtle.register_shape("Resources\\Left_Facing_Shaun.gif")
        turtle.register_shape("Resources\\Right_Facing_Shaun.gif")
        turtle.register_shape("Resources\\Wall.gif")
        turtle.register_shape("Resources\\Gun.gif")
        turtle.register_shape("Resources\\Down_Arrow.gif")
        turtle.register_shape("Resources\\Left_Arrow.gif")
        turtle.register_shape("Resources\\Right_Arrow.gif")
        turtle.register_shape("Resources\\Up_Arrow.gif")   #new remove a /

        #Define the screen
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Shaun of the Dead")
        self.wn.setup(700,700)

        #Create items from classes
        self.level_key = self.gameStateManager.get("Current_Level")
        self.wallBlock = wall_block_.WallBlock()
        self.player = game_player_.Player(self.gameStateManager)
        #self.treasure_bullets = treasure_.Treasure_Bullets()
        #self.treasure_lives = treasure_.Treasure_Lives()
        self.enemy_list = enemy_list_.EnemyList(self.gameStateManager)
        self.wall_block_list = wall_block_list_.WallBlockList(self.gameStateManager)
        self.npc_list = npc_list_.NPCList(self.gameStateManager)
        self.treasure_lives_list = treasure_lives_list_.TreasureLivesList(self.gameStateManager)
        self.treasure_bullets_list = treasure_bullets_list_.TreasureBulletsList(self.gameStateManager)
        self.fences_list = fences_list_.FencesList(self.gameStateManager)

        if start_mode.upper()== "N":
            self.level_key="1"

        #Create Lists
        self.npc_list.fill_npc_list()
        self.enemy_list.fill_enemy_list()
        self.wall_block_list.fill_wall_list()
        self.treasure_lives_list.fill_treasure_lives_list()
        self.treasure_bullets_list.fill_treasure_bullets_list()
        self.fences_list.fill_fences_list()

        self.walls = []
        self.bullets = []
        self.fences = []

        self.player.walls = self.walls

        for player in self.npc_list.npc_list:
            player.walls = self.walls
            
        #Listen to keyboard input
        turtle.listen()
        turtle.onkey(self.player.go_left,"a")
        turtle.onkey(self.player.go_right,'d')
        turtle.onkey(self.player.go_up,'w')
        turtle.onkey(self.player.go_down,'s')
        turtle.onkey(self.fire_bullet,'f')
        turtle.onkey(self.quit_game,'q')
        self.wn.tracer(0)

        self.setup_level()

#Everything above line this is preparing objects
###############################
#Everything below line runs the game

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

            for treasure_bullet in self.treasure_bullets_list.treasure_bullets_list:
                if self.player.is_collision_with_treasure_bullets(treasure_bullet):
                    self.player.bullets += treasure_bullet.GetBullets("UnLimited")
                    #Save player.bullets state
                    self.gameStateManager.set("bullets" , self.player.bullets) #new
                    print ("Shaun has " + str(self.player.bullets) + " bullets")

            for treasure_life in self.treasure_lives_list.treasure_lives_list:
                if self.player.is_collision_with_treasure_lives(treasure_life):
                    self.player.lives += treasure_life.lives
                    #Save player.lives state
                    self.gameStateManager.set("lives" , self.player.lives) #new
                    print ("Shaun has gained a life")
                    print ("Shaun has " + str(self.player.lives) + " lives")

            self.moveEnemies()
            self.moveNPC()
            self.movebullets()
            self.wn.update()

        self.wn.bye()
            

    
    
