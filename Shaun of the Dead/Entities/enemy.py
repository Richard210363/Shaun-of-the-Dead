import turtle
import math
import random
import datetime
import constant
import time

import Maths.Bresenham as bres_
import ListManagement.sprite_list_manager as sprite_list_manager_

class Enemy(turtle.Turtle):
    def __init__(self, x, y, enemyType, name, lives, gameStateManager, enemy_list):
        turtle.Turtle.__init__(self)
        self.shape('Resources\\Zombie.gif')
        self.color('orange')
        self.penup()
        self.speed(0)
        self.gold = 25
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.can_kill = True
        self.then_move=datetime.datetime.now()
        self.name = name
        self.then_collision=datetime.datetime.now()
        self.closeFlag = False
        self.can_chase = False
        self.lives=lives
        self.type=enemyType
        self.x_cor=x
        self.y_cor=y
        self.gameStateManager=gameStateManager
        self.enemy_list=enemy_list
        self.current_frame = 0
        self.female_enemy_die_list = []
        self.female_enemy_go_right_list = []
        self.female_enemy_go_left_list = []
        self.female_enemy_go_up_list = []
        self.female_enemy_go_down_list = []

    def get_female_enemy_die_list(self):
        '''Preparing list for animation'''
        self.female_enemy_die_list = sprite_list_manager_.load_images(constant.female_enemy_die_animation)

    def get_female_enemy_go_right_list(self):
        '''Preparing list for animation'''
        self.female_enemy_go_right_list = sprite_list_manager_.load_images(constant.female_enemy_animation_right_injury_0)

    def get_female_enemy_go_left_list(self):
        '''Preparing list for animation'''
        self.female_enemy_go_left_list = sprite_list_manager_.load_images(constant.female_enemy_animation_left_injury_0)

    def get_female_enemy_go_up_list(self):
        '''Preparing list for animation'''
        self.female_enemy_go_up_list = sprite_list_manager_.load_images(constant.female_enemy_animation_up_injury_0)

    def get_female_enemy_go_down_list(self):
        '''Preparing list for animation'''
        self.female_enemy_go_down_list = sprite_list_manager_.load_images(constant.female_enemy_animation_down_injury_0)

    def initialise(self):
        '''Prepares player for use'''
        self.get_female_enemy_die_list()
        self.get_female_enemy_go_right_list()
        self.get_female_enemy_go_left_list()
        self.get_female_enemy_go_up_list()
        self.get_female_enemy_go_down_list()

    def destroy(self, wn):
        for position in range(len(self.female_enemy_die_list) - 1):
            filename = self.female_enemy_die_list[position]
            self.shape(constant.female_enemy_die_animation + "\\" + filename)
            wn.update()
            time.sleep(0.25)
        self.goto(2000,2000)
        self.hideturtle()

    def wound(self, wn):
        self.lives -=1
        if self.lives <= 0:
            self.destroy(wn)
            #print ("Shaun killed a zombie!")
            self.enemy_list.remove_enemy_from_list(self)
        self.gameStateManager.updateZombie(self.name,self.lives)

 
#Is the player close to self?  Triggers the hunting response
    def is_close(self, other, walls):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
       
        distance = math.sqrt((a ** 2) + (b ** 2) )
        if distance > 150:
            return False

        print("======================================")
        print ("enemy close to player")
        bres = bres_.Bresenham([self.xcor()/24, self.ycor()/24], [other.xcor()/24, other.ycor()/24])
        while not bres.finished():
            p = bres.get_next()
            #print("x" + str(p[0]*24))
            #print("y" + str(p[1]*24))
            if((p[0]*24,p[1]*24)) in walls:
                print ("Wall in the way")
                return False
        print ("Wall not in the way")
        return True

#Move sprite
    def move(self,player,walls,fences):

#Set the speed of Enemy movement by not moving in too short a time period
        now_move=datetime.datetime.now()      
        diff_move = now_move - self.then_move

#Determine how long it is since the last collision
        now_collision=datetime.datetime.now()      
        diff_collision = now_collision - self.then_collision

#Set the can chase flag based on how long its been since a collision
        if self.can_chase==False:
            if diff_collision.seconds>2:
                if player.has_entered_safe_area==True:
                    self.can_chase=True


        #print("Difference:", diff)
        #print("Days:", diff.days)
        #print("Microseconds:", diff.microseconds)
        #print("Seconds:", diff.seconds)

        if diff_move.microseconds<300000:  # Set Enemy speed here. Lower is faster
            return

        self.then_move=now_move

#Is a player close enough to interact with        
        if self.can_chase==True:
            print("Can Chase Shaun")
            self.closeFlag = False
            if self.is_close(player, walls):
                print("Chasing Shaun")
                if player.xcor() < self.xcor():
                    self.direction = 'left'
                if player.xcor() > self.xcor():
                    self.direction = 'right'
                if player.ycor() < self.ycor():
                    self.direction = 'down'
                if player.ycor() > self.ycor():
                    self.direction = 'up'
                self.closeFlag = True
        else:
            print("Can't Chase Shaun Yet")
            self.closeFlag = False


#Set sprite picture and movement deltas
        if self.direction == 'up':
            dx = 0
            dy = 24
            print("zombie: " + str(self.name) + "    " + str(len(self.female_enemy_go_up_list)))
            print("zombie: " + str(self.name) + "    " + str(self.current_frame))
            print("zombie: " + str(self.name) + "    " + "About to go up")
            filename = self.female_enemy_go_up_list[self.current_frame]
            print("zombie: " + str(self.name) + "    " + "Has gone up")
            self.current_frame = self.current_frame + 1
            if self.current_frame >= len(self.female_enemy_go_up_list) - 1:
                self.current_frame = 0
            self.shape(constant.female_enemy_animation_up_injury_0 + "\\" + filename)
        elif self.direction == 'down':
            dx = 0
            dy = -24
            print("zombie: " + str(self.name) + "    " + str(len(self.female_enemy_go_down_list)))
            print("zombie: " + str(self.name) + "    " + str(self.current_frame))
            print("zombie: " + str(self.name) + "    " + "About to go down")
            filename = self.female_enemy_go_down_list[self.current_frame]
            print("zombie: " + str(self.name) + "    " + "Has gone down")
            self.current_frame = self.current_frame + 1
            if self.current_frame >= len(self.female_enemy_go_down_list) - 1:
                self.current_frame = 0
            self.shape(constant.female_enemy_animation_down_injury_0 + "\\" + filename)
        elif self.direction == 'left':
            dx = -24
            dy = 0
            print("zombie: " + str(self.name) + "    " + str(len(self.female_enemy_go_left_list)))
            print("zombie: " + str(self.name) + "    " + str(self.current_frame))
            print("zombie: " + str(self.name) + "    " + "About to go left")
            filename = self.female_enemy_go_left_list[self.current_frame]
            print("zombie: " + str(self.name) + "    " + "Has gone left")
            self.current_frame = self.current_frame + 1
            if self.current_frame >= len(self.female_enemy_go_left_list) - 1:
                self.current_frame = 0
            self.shape(constant.female_enemy_animation_left_injury_0 + "\\" + filename)
        elif self.direction == 'right':
            dx = 24
            dy = 0
            print("zombie: " + str(self.name) + "    " + str(len(self.female_enemy_go_right_list)))
            print("zombie: " + str(self.name) + "    " + str(self.current_frame))
            print("zombie: " + str(self.name) + "    " + "About to go right")
            filename = self.female_enemy_go_right_list[self.current_frame]
            print("zombie: " + str(self.name) + "    " + "Has gone right")
            self.current_frame = self.current_frame + 1
            if self.current_frame >= len(self.female_enemy_go_right_list) - 1:
                self.current_frame = 0
            self.shape(constant.female_enemy_animation_right_injury_0 + "\\" + filename)
        else:
            dx = 0
            dy = 0
            filename = self.female_enemy_go_down_list[0]
            self.shape(constant.female_enemy_animation_down_injury_0 + "\\" + filename)

#Move
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            if (move_to_x, move_to_y) not in fences:

                self.goto(move_to_x, move_to_y)


#Set direction for next iteration
        if self.closeFlag == False:
            self.direction = random.choice(['up', 'down', 'left', 'right'])

#Have we hit a player?
#Enemies must leave a player before they can be hit again 
    def is_collision_with_player(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_kill=True

        if self.can_kill:
            if distance < 5:
                self.can_chase = False
                self.then_collision=datetime.datetime.now() 
                self.can_kill=False

                return True
            else:
                return False
