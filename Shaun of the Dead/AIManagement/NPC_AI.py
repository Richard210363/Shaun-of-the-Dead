import random
import math
import Maths.Bresenham as bres_

class NPC_AI(object):
    """description of class"""
    def __init__(self):
        self.direction=""
        self.direction_loop_list = ["x", "x", "x", "x"]
        self.randomly = random.randint(1,10000000)

    def get_direction_random(self):
        self.direction = random.choice(['go_up', 'go_down', 'go_left', 'go_right'])
        return self.direction

    def found_Shaun(self, NPC, player, walls):
        a=NPC.xcor() - player.xcor()
        b = NPC.ycor() - player.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 72:
            return False

        print("======================================")
        print ("NPC close to player")
        bres = bres_.Bresenham([NPC.xcor()/24, NPC.ycor()/24], [player.xcor()/24, player.ycor()/24])
        while not bres.finished():
            p = bres.get_next()
            #print("x" + str(p[0]*24))
            #print("y" + str(p[1]*24))
            if((p[0]*24,p[1]*24)) in walls:
                print ("Wall in the way")
                return False
        print ("Wall not in the way")
        return True

    def follow_Shaun(self, NPC, player):
        NPC.direction = player.direction

    def found_enemy(self, NPC, enemy, walls):
        a=NPC.xcor() - enemy.xcor()
        b = NPC.ycor() - enemy.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 144:
            return False
        
        print("======================================")
        print ("NPC close to enemy")
        bres = bres_.Bresenham([NPC.xcor()/24, NPC.ycor()/24], [enemy.xcor()/24, enemy.ycor()/24])
        while not bres.finished():
            p = bres.get_next()
            #print("x" + str(p[0]*24))
            #print("y" + str(p[1]*24))
            if((p[0]*24,p[1]*24)) in walls:
                print ("Wall in the way")
                return False
        print ("Wall not in the way")
        return True

    def enemy_too_close(self, NPC, enemy):
        a=NPC.xcor() - enemy.xcor()
        b = NPC.ycor() - enemy.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 48:
            return False
        return True

    def orientate_towards_enemy(self, NPC, enemy):
        if enemy.xcor() > NPC.xcor():
            NPC.direction = "go_right"
        elif enemy.xcor() < NPC.xcor():
            NPC.direction = "go_left"
        elif enemy.ycor() > NPC.ycor():
            NPC.direction = "go_up"        
        elif enemy.ycor() < NPC.ycor():
            NPC.direction = "go_down"

    def reverse_orientation(self, NPC):
        if NPC.direction == "go_left":
            NPC.direction = "go_right"
        elif NPC.direction == "go_right":
            NPC.direction = "go_left"
        elif NPC.direction == "go_up":
            NPC.direction = "go_down"
        elif NPC.direction == "go_down":
            NPC.direction = "go_up"            

    def set_direction_loop_list(self, direction):
        self.direction_loop_list[0] = self.direction_loop_list[1]
        self.direction_loop_list[1] = self.direction_loop_list[2]
        self.direction_loop_list[2] = self.direction_loop_list[3]
        self.direction_loop_list[3] = direction
        pass

    def loop_detected(self):
        if self.direction_loop_list[0] == "go_right" and self.direction_loop_list[1] == "go_up" and self.direction_loop_list[2] == "go_left" and self.direction_loop_list[3] == "go_down":
            return True
        else:
            return False

    def set_NPC_direction(self,NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC,player):
        #print("Begin print - " + str(self.randomly))
        #print("NPC.x_cor - " + str(NPC.x_cor))
        #print("NPC.y_cor - " + str(NPC.y_cor))
        #print("NPC_left_x - " + str(NPC_left_x))
        #print("NPC_left_y - " + str(NPC_left_y))
        #print("NPC_forward_x - " + str(NPC_forward_x))
        #print("NPC_forward_y - " + str(NPC_forward_y))
        #print("End print")
        if(NPC_left_x,NPC_left_y) not in NPC.walls:
            if NPC.direction == "go_left":
                self.set_direction_loop_list("go_down")
                if not self.loop_detected():
                    NPC.direction = "go_down"
                else:
                    NPC.direction = "go_up"
            elif NPC.direction == "go_right":
                self.set_direction_loop_list("go_up")
                if not self.loop_detected():
                    NPC.direction = "go_up"
                else:
                    NPC.direction = "go_down"
            elif NPC.direction == "go_up":
                self.set_direction_loop_list("go_left")
                if not self.loop_detected():
                    NPC.direction = "go_left"
                else:
                    NPC.direction ="go_right"
            elif NPC.direction == "go_down":
                self.set_direction_loop_list("go_right")
                if not self.loop_detected():
                    NPC.direction = "go_right"
                else:
                    NPC.direction = "go_left"
            return

        if (NPC_forward_x,NPC_forward_y) in NPC.walls:
            if NPC.direction == "go_left":
                self.set_direction_loop_list("go_up")
                if not self.loop_detected():
                    NPC.direction = "go_up"
                else:
                    NPC.direction = "go_down"
            elif NPC.direction == "go_right":
                self.set_direction_loop_list("go_down")
                if not self.loop_detected():
                    NPC.direction = "go_down"
                else:
                    NPC.direction = "go_up"
            elif NPC.direction == "go_up":
                self.set_direction_loop_list("go_right")
                if not self.loop_detected():
                    NPC.direction = "go_right"
                else:
                    NPC.direction = "go_left"
            elif NPC.direction == "go_down":
                self.set_direction_loop_list("go_left")
                if not self.loop_detected():
                    NPC.direction = "go_left"
                else:
                    NPC.direction = "go_right"
            return
        else:
            self.direction_loop_list = ["x", "x", "x", "x"]
            return

    def get_direction_searching(self, NPC, player):
        pass
        if NPC.direction == "go_left":
            #NL = "down" x is same y is 24 less than NPC.y_cor
            NPC_left_x = NPC.x_cor
            NPC_left_y = NPC.y_cor-24
            NPC_forward_x = NPC.x_cor-24
            NPC_forward_y = NPC.y_cor
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC,player)
        elif NPC.direction == "go_right":
            NPC_left_x = NPC.x_cor
            NPC_left_y = NPC.y_cor+24
            NPC_forward_x = NPC.x_cor+24
            NPC_forward_y = NPC.y_cor
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC,player)
        elif NPC.direction == "go_up":
            NPC_left_x = NPC.x_cor-24
            NPC_left_y = NPC.y_cor
            NPC_forward_x = NPC.x_cor
            NPC_forward_y = NPC.y_cor+24
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC,player)
        elif NPC.direction == "go_down":
            NPC_left_x = NPC.x_cor+24
            NPC_left_y = NPC.y_cor
            NPC_forward_x = NPC.x_cor
            NPC_forward_y = NPC.y_cor-24
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC,player)

        #if NPC doesn't have a wall left then turn left
        #    if NPC doesn't have a space in front then turn right
        #        else go forward

