import turtle
import math

import Entities.player as player

class Bullet(turtle.Turtle):
    def __init__(self,current_player,walls):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.direction = ""
        self.current_player = current_player
        self.walls = walls

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

    #Define Bullet Movement
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in self.walls:
            self.destroy()
   
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in self.walls:
            self.destroy()

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in self.walls:
            self.destroy()
   
    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in self.walls:
            self.destroy()

    def move(self):
        if(self.direction=="go_up"):
            self.go_up()
        if(self.direction=="go_down"):
            self.go_down()
        if(self.direction=="go_left"):
            self.go_left()
        if(self.direction=="go_right"):
            self.go_right()
           
        ##Set timer event
        #turtle.ontimer(self.move, t=250)

    def set_direction(self):
        move_to_x = self.current_player.xcor()
        move_to_y = self.current_player.ycor()
        self.goto(move_to_x,move_to_y)
        if(self.current_player.direction=="go_up"):
            self.direction="go_up"
        if(self.current_player.direction=="go_down"):
            self.direction="go_down"
        if(self.current_player.direction=="go_left"):
            self.direction="go_left"
        if(self.current_player.direction=="go_right"):
            self.direction="go_right"
        self.move()

    def is_collision(self, enemy):
        a=self.xcor() - enemy.xcor()
        b = self.ycor() - enemy.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance < 5:
            return True
        else:
            return False
