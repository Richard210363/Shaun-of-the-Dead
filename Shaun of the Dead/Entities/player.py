import turtle
import math
import ListManagement.sprite_list_manager as sprite_list_manager_
import constant

class Player(turtle.Turtle):
    def __init__(self, gameStateManager):
        turtle.Turtle.__init__(self)
        player_from_database = gameStateManager.get("Player")
        self.bullets=player_from_database["bullets"]
        self.lives=player_from_database["lives"]
        self.x_cor=player_from_database["x_cor"]
        self.y_cor=player_from_database["y_cor"]
        self.name=player_from_database["name"]
        self.shape("Resources\\Shaun.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.direction="go_down"
        self.can_get_bullets=True
        self.can_get_lives=True
        self.has_entered_safe_area=False
        self.walls = []
        self.safe_area = []
        self.go_right_list = []
        self.go_left_list = []
        self.go_up_list = []
        self.go_down_list = []
        self.current_frame = 0
        self.gameStateManager=gameStateManager

    def check_entered_safe_area(self,move_to_x,move_to_y):
        if self.has_entered_safe_area == False:
            if (move_to_x,move_to_y) in self.safe_area:
                self.has_entered_safe_area = True

    def get_go_right_list(self):
        '''Preparing list for animation'''
        self.go_right_list = sprite_list_manager_.load_images(constant.shaun_animation_right)

    def get_go_left_list(self):
        '''Preparing list for animation'''
        self.go_left_list = sprite_list_manager_.load_images(constant.shaun_animation_left)

    def get_go_up_list(self):
        '''Preparing list for animation'''
        self.go_up_list = sprite_list_manager_.load_images(constant.shaun_animation_up)

    def get_go_down_list(self):
        '''Preparing list for animation'''
        self.go_down_list = sprite_list_manager_.load_images(constant.shaun_animation_down)

    def initialise(self):
        '''Prepares player for use'''
        self.get_go_right_list()
        self.get_go_left_list()
        self.get_go_up_list()
        self.get_go_down_list()

    #Define Player Movement
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Resources\\Shaun.gif")
            self.direction="go_up"
            self.check_entered_safe_area(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Resources\\Shaun.gif")
            self.direction="go_down"
            self.check_entered_safe_area(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Resources\\Left_Facing_Shaun.gif")
            self.direction="go_left"
            self.check_entered_safe_area(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Resources\\Right_Facing_Shaun.gif")
            self.direction="go_right"
            self.check_entered_safe_area(move_to_x,move_to_y)
   
    #Define Player Events          
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
