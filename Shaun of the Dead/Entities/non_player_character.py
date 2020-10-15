import turtle
import math
import datetime

import AIManagement.NPC_AI as NPC_AI
import Entities.bullet as bullet
import ResourceManagement.sound_effects as sound_effect

class NPC(turtle.Turtle):
    def __init__(self, x, y, bullets, name, lives, gameStateManager):
        turtle.Turtle.__init__(self)
        self.x_cor=x
        self.y_cor=y
        self.name=name        
        self.bullets=bullets      
        self.lives=lives
        self.shape("Resources\\Up_Arrow.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.direction="go_down"
        self.can_get_bullets=True
        self.can_get_lives=True
        self.walls = []
        self.gameStateManager=gameStateManager
        self.then_move=datetime.datetime.now()
        self.then_fire_bullet = datetime.datetime.now()
        self.NPC_AI = NPC_AI.NPC_AI()

    #Define NPC Events   
    # def is_collision_with_treasure_bullets(self, other):         
    def is_collision_with_treasure_bullets(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_get_bullets=True
            #print ("Distance > 10")
            #print (distance)

        if self.can_get_bullets:
            if distance < 5:
                self.can_get_bullets=False
                #print ("Distance < 5")
                #print (distance)
                return True
            else:
                return False

    def is_collision_with_treasure_lives(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_get_lives=True
            #print ("Distance > 10")
            #print (distance)

        if self.can_get_lives:
            if distance < 5:
                self.can_get_lives=False
                #print ("Distance < 5")
                #print (distance)
                return True
            else:
                return False

#Move sprite
    def move(self, walls, player, enemies, bullets): #do we really want to pass the player to an NPC?

#Set the speed of NPC movement by not moving in too short a time period
        now_move=datetime.datetime.now()      
        diff_move = now_move - self.then_move

        if diff_move.microseconds<300000:  # Set NPC speed here. Lower is faster
            return

        self.then_move=now_move

#Calculate direction
        enemy_is_close = False
        can_kill_enemy = False
        for enemy in enemies:
            if self.NPC_AI.found_enemy(self, enemy, walls):
                self.NPC_AI.orientate_towards_enemy(self, enemy) 
                enemy_is_close = True
                can_kill_enemy = False
                break

        for enemy in enemies:
            if self.NPC_AI.enemy_too_close(self, enemy):
                self.NPC_AI.reverse_orientation(self)
                can_kill_enemy = False

        if enemy_is_close == False:
            self.NPC_AI.get_direction_searching(self, player)

        if self.NPC_AI.found_Shaun(self, player, walls):
            self.NPC_AI.follow_Shaun(self, player)

#Set sprite picture and movement deltas
        if self.direction == 'go_up':
            dx = 0
            dy = 24
            self.shape("Resources\\Up_Arrow.gif")
        elif self.direction == 'go_down':
            dx = 0
            dy = -24
            self.shape("Resources\\Down_Arrow.gif")
        elif self.direction == 'go_left':
            dx = -24
            dy = 0
            self.shape("Resources\\Left_Arrow.gif")
        elif self.direction == 'go_right':
            dx = 24
            dy = 0
            self.shape("Resources\\Right_Arrow.gif")
        else:
            dx = 0
            dy = 0
            self.shape("Resources\\Up_Arrow.gif")

#Move
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            self.x_cor = move_to_x
            self.y_cor = move_to_y

        now_fire_bullet=datetime.datetime.now()      
        diff_fire_bullet = now_fire_bullet - self.then_fire_bullet

        if diff_fire_bullet.microseconds<900000:
            return

        self.then_fire_bullet=now_fire_bullet

        if can_kill_enemy:
            current_bullet = bullet.Bullet(self, walls)
            bullets.append(current_bullet)
            current_bullet.set_direction()
            sound_effect.bulletSound.play()



##Set direction for next iteration
#        self.direction = self.NPC_AI.get_direction_random()