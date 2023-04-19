import pygame
from maplvl1 import *

class Player:

    def __init__(self):
        self.life = 3
        self.score = 0
        self.death = 0


class Pacman(Player):

    def __init__(self):

        Player.__init__(self)

        self.pacy = pygame.image.load("img/pac2.png").convert_alpha()

        self.pac_sprite_r = []
        self.pac_sprite_r += [pygame.image.load("img/pac.png").convert_alpha()]
        self.pac_sprite_r += [self.pacy]

        self.pac_sprite_l = []
        self.pac_sprite_l += [pygame.image.load("img/pac3.png").convert_alpha()]
        self.pac_sprite_l += [self.pacy]

        self.pac_sprite_u = []
        self.pac_sprite_u += [pygame.image.load("img/pac4.png").convert_alpha()]
        self.pac_sprite_u += [self.pacy]

        self.pac_sprite_d = []
        self.pac_sprite_d += [pygame.image.load("img/pac5.png").convert_alpha()]
        self.pac_sprite_d += [self.pacy]

        self.w = 50
        self.h = 50

        self.posX = 50
        self.posY = 50
        self.ind_point = 0
        self.next_point = 0;

        self.indleft = 0
        self.indright = 0
        self.indup = 0
        self.inddown = 0

        self.time_change = pygame.time.get_ticks()
        self.time_change_pos = pygame.time.get_ticks()
               
        self.move_left = 0
        self.move_right = 0
        self.move_up = 0
        self.move_down = 0

        self.start = 1

    def get(self, ind):
        return self.pac_sprite[ind]

    def set_right(self):
        self.indright = (self.indright + 1) % 2

    def get_right(self):
        return self.pac_sprite_r[self.indright]

    def set_left(self):
        self.indleft = (self.indleft + 1) % 2

    def get_left(self):
        return self.pac_sprite_l[self.indleft]

    def set_up(self):
        self.indup = (self.indup + 1) % 2

    def get_up(self):
        return self.pac_sprite_u[self.indup]

    def set_down(self):
        self.inddown = (self.inddown + 1) % 2

    def get_down(self):
        return self.pac_sprite_d[self.inddown]

    def change_dir(self, ml, d):

        if self.move_right:
            if d == 3:
                self.move_up = 0
                self.move_right = 1
                self.move_left = 0
                self.move_down = 0
                self.next_point = ml.neigh[self.ind_point][3]
                return
            if d == 2:
                #if ml.neigh[self.ind_point][2] != -1:
                    self.move_up = 0
                    self.move_right = 0
                    self.move_left = 1
                    self.move_down = 0
                    #self.ind_point = ml.neigh[self.ind_point][3]
                    if self.next_point != 50:
                        self.ind_point, self.next_point = self.next_point, self.ind_point
                    else:
                        self.next_point = ml.neigh[self.ind_point][2]
                    return 

            #if ml.neigh[self.ind_point][3] != -1:
            ng = self.next_point
            if ng == 50:
                ng = self.ind_point
            if self.posX >= ml.turn_point[ng][0]-30 and self.posX <= ml.turn_point[ng][0]+30:
                if d == 0:
                    #if ml.neigh[self.ind_point][0] != -1:
                    self.posX = ml.turn_point[ng][0]
                    self.move_up = 1
                    self.move_right = 0
                    self.move_left = 0
                    self.move_down = 0
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][0]
                elif d == 1:
                    #if ml.neigh[self.ind_point][1] != -1:
                    self.posX = ml.turn_point[ng][0]
                    self.move_up = 0
                    self.move_right = 0
                    self.move_left = 0
                    self.move_down = 1
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][1]

        elif self.move_left:

            if d == 2:
                self.move_up = 0
                self.move_right = 0
                self.move_left = 1
                self.move_down = 0
                self.next_point = ml.neigh[self.ind_point][2]
                return 

            if d == 3:
                #if ml.neigh[self.ind_point][3] != -1:
                self.move_up = 0
                self.move_right = 1
                self.move_left = 0
                self.move_down = 0
                #self.ind_point = ml.neigh[self.ind_point][3]
                if self.next_point != 50:
                    self.ind_point, self.next_point = self.next_point, self.ind_point
                else:
                    self.next_point = ml.neigh[self.ind_point][3]
                return
            
            #if ml.neigh[self.ind_point][2] != -1:
            ng = self.next_point
            if ng == 50:
                ng = self.ind_point
            if self.posX >= ml.turn_point[ng][0]-30 and self.posX <= ml.turn_point[ng][0]+30:
                if d == 0:
                    #if ml.neigh[self.ind_point][0] != -1:
                    self.posX = ml.turn_point[ng][0]
                    self.move_up = 1
                    self.move_right = 0
                    self.move_left = 0
                    self.move_down = 0
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][0]
                elif d == 1:
                    #if ml.neigh[self.ind_point][1] != -1:
                    self.posX = ml.turn_point[ng][0]
                    self.move_up = 0
                    self.move_right = 0
                    self.move_left = 0
                    self.move_down = 1
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][1]
                            

        elif self.move_down:
            if d == 1:
                #if ml.neigh[self.ind_point][0] != -1:
                self.move_up = 0
                self.move_right = 0
                self.move_left = 0
                self.move_down = 1
                self.next_point = ml.neigh[self.ind_point][1]
                return

            if d == 0:
                #if ml.neigh[self.ind_point][0] != -1:
                self.move_up = 1
                self.move_right = 0
                self.move_left = 0
                self.move_down = 0
                if self.next_point != 50:
                    self.ind_point, self.next_point = self.next_point, self.ind_point
                else:
                    self.next_point = ml.neigh[self.ind_point][0]
                return
            
            #if ml.neigh[self.ind_point][1] != -1:
            ng = self.next_point
            if ng == 50:
                ng = self.ind_point
            if self.posY >= ml.turn_point[ng][1]-30 and self.posY <= ml.turn_point[ng][1]+30:
                if d == 2:
                    #if ml.neigh[self.ind_point][2] != -1:
                    self.posY = ml.turn_point[ng][1]
                    self.move_up = 0
                    self.move_right = 0
                    self.move_left = 1
                    self.move_down = 0
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][2]
                elif d == 3:
                    #if ml.neigh[self.ind_point][3] != -1:
                    self.posY = ml.turn_point[ng][1]
                    self.move_up = 0
                    self.move_right = 1
                    self.move_left = 0
                    self.move_down = 0
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][3]

        elif self.move_up:
            if d == 0:
                #if ml.neigh[self.ind_point][1] != -1:
                self.move_up = 1
                self.move_right = 0
                self.move_left = 0
                self.move_down = 0
                self.next_point = ml.neigh[self.ind_point][0]
                return

            if d == 1:
                #if ml.neigh[self.ind_point][1] != -1:
                self.move_up = 0
                self.move_right = 0
                self.move_left = 0
                self.move_down = 1
                if self.next_point != 50:
                    self.ind_point, self.next_point = self.next_point, self.ind_point
                else:
                    self.next_point = ml.neigh[self.ind_point][1]
                return
            
            #if ml.neigh[self.ind_point][0] != -1:
            ng = self.next_point
            if ng == 50:
                ng = self.ind_point
            if self.posY >= ml.turn_point[ng][1]-30 and self.posY <= ml.turn_point[ng][1]+30:
                if d == 2:
                    #if ml.neigh[self.ind_point][2] != -1:
                    self.posY = ml.turn_point[ng][1]
                    self.move_up = 0
                    self.move_right = 0
                    self.move_left = 1
                    self.move_down = 0
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][2]
                elif d == 3:
                    #if ml.neigh[self.ind_point][3] != -1:
                    self.posY = ml.turn_point[ng][1]
                    self.move_up = 0
                    self.move_right = 1
                    self.move_left = 0
                    self.move_down = 0
                    if self.next_point == 50:
                        self.next_point = ml.neigh[self.ind_point][3]   

        

    def update_pos(self, ml, freeze):
    
        if self.move_right:
            #print("right " + str (ml.neigh[self.ind_point][3]))
            #if ml.neigh[self.ind_point][3] != -1:
            ng = self.next_point
            if ng != 50 and self.posX < ml.turn_point[ng][0]:
                if not freeze:
                    t = pygame.time.get_ticks() - self.time_change_pos
                    self.posX += t * 40.0 / 250.0
                    
            else:
                if self.next_point != 50:
                    self.ind_point= self.next_point
                    self.next_point = ml.neigh[self.next_point][3]

        elif self.move_left:
            #if ml.neigh[self.ind_point][2] != -1:
            #print(self.ind_point)
            ng = self.next_point
            if ng != 50 and self.posX > ml.turn_point[ng][0]:
                if not freeze:
                    t = pygame.time.get_ticks() - self.time_change_pos
                    self.posX -= t * 40.0 / 250.0
                    
            else:
                
                if self.next_point != 50:
                    self.ind_point= self.next_point
                    self.next_point = ml.neigh[self.next_point][2]

        elif self.move_down:
            #if ml.neigh[self.ind_point][1] != -1:
            ng = self.next_point
            if ng != 50 and self.posY < ml.turn_point[ng][1]:
                if not freeze:
                    t = pygame.time.get_ticks() - self.time_change_pos
                    self.posY += t * 40.0 / 250.0
                    
            else:
               
                if self.next_point != 50:
                    self.ind_point= self.next_point
                    self.next_point = ml.neigh[self.next_point][1]

        elif self.move_up:
            #if ml.neigh[self.ind_point][0] != -1:
            ng = self.next_point
            if ng != 50 and self.posY > ml.turn_point[ng][1]:
                if not freeze:
                    t = pygame.time.get_ticks() - self.time_change_pos
                    self.posY -= t * 40.0 / 250.0
                    
            else:
             
                if self.next_point != 50:
                    self.ind_point= self.next_point
                    self.next_point = ml.neigh[self.next_point][0]
           
           
        self.time_change_pos = pygame.time.get_ticks()

        #print(str(self.move_up) + " " + str(self.move_down) + " " + str(self.move_left) + " " + str(self.move_right))
        #print(str(self.ind_point) + " " + str(self.next_point))

    def display(self, screen):
               
        
        if self.start or self.move_right:
            t = pygame.time.get_ticks() - self.time_change
            if t >= 250:
			    self.set_right()
			    self.time_change = pygame.time.get_ticks()
            screen.blit(self.get_right(), (self.posX-25, self.posY-25)) 
         
        elif self.move_left:
            t = pygame.time.get_ticks() - self.time_change
            if t >= 250:
                self.set_left()
                self.time_change = pygame.time.get_ticks()
            screen.blit(self.get_left(), (self.posX-25, self.posY-25)) 
        
        elif self.move_down:
            t = pygame.time.get_ticks() - self.time_change
            if t >= 250:
                self.set_down()
                self.time_change = pygame.time.get_ticks()
            screen.blit(self.get_down(), (self.posX-25, self.posY-25)) 
         
        elif self.move_up:
            t = pygame.time.get_ticks() - self.time_change
            if t >= 250:
                self.set_up()
                self.time_change = pygame.time.get_ticks()
            screen.blit(self.get_up(), (self.posX-25, self.posY-25)) 
         
        