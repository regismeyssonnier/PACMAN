import pygame
import sys
import math
from playsound import playsound
import threading

def distance(x, y, x2, y2):
    return math.sqrt((x-x2)**2 + (y-y2)**2)

class MapLvl1:

    def __init__(self):

        self.w = 1800
        self.h = 800

        self.maplvl1 = pygame.image.load("img/maplvl1.png").convert_alpha()
        self.gemsp = pygame.image.load("img/gem.png").convert_alpha()

        self.turn_point = [
          (50, 50),
          (50, 250),
          (50, 450),
          (50, 650),

          (450, 50),
          (450, 250),
          (450, 450),
          (450, 650),
            
          (570, 50),
          (570, 250),
          (570, 450),
          (570, 650),
            
          (785, 50),
          (785, 250),
          (785, 450),
          (785, 650),

          (1015, 50),
          (1015, 250),
          (1015, 450),
          (1015, 650),

          (1230, 50),
          (1230, 250),
          (1230, 450),
          (1230, 650),
            
          (1350, 50),
          (1350, 250),
          (1350, 450),
          (1350, 650),

          (1750, 50),
          (1750, 250),
          (1750, 450),
          (1750, 650)
                      
        ]

        self.dif_point = [
           #[U, D, L, R]
            [0, 1, 0, 1],
            [1, 1, 0, 1],   
            [1, 1, 0, 1],
            [1, 0, 0, 1],

            [0, 1, 1, 1],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 0, 1, 1],

            [0, 1, 1, 1],
            [1, 1, 0, 1],   
            [1, 1, 0, 1],
            [1, 0, 1, 1],

            [0, 1, 1, 1],
            [1, 1, 1, 1],   
            [1, 1, 1, 1],
            [1, 0, 1, 1],

            [0, 1, 1, 1],
            [1, 1, 1, 1],   
            [1, 1, 1, 1],
            [1, 0, 1, 1],

            [0, 1, 1, 1],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 0, 1, 1],

            [0, 1, 1, 1],
            [1, 1, 0, 1],   
            [1, 1, 0, 1],
            [1, 0, 1, 1],

            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 0, 1, 0]



        ]

        self.neigh = [
            [50, 1, 50, 4],
            [0, 2, 50, 5],   
            [1, 3, 50, 6],
            [2, 50, 50, 7],

            [50, 5, 0, 8],
            [4, 6, 1, 50],
            [5, 7, 2, 50],
            [6, 50, 3, 11],

            [50, 9, 4, 12],
            [8, 10, 50, 13],   
            [9, 11, 50, 14],
            [10, 50, 7, 15],

            [50, 13, 8, 16],
            [12, 14, 9, 17],   
            [13, 15, 10, 18],
            [14, 50, 11, 19],

            [50, 17, 12, 20],
            [16, 18, 13, 21],   
            [17, 19, 14, 22],
            [18, 50, 15, 23],

            [50, 21, 16, 24],
            [20, 22, 17, 50],
            [21, 23, 18, 50],
            [22, 50, 19, 27],

            [50, 25, 20, 28],
            [24, 26, 50, 29],   
            [25, 27, 50, 30],
            [26, 50, 23, 31],

            [50, 29, 24, 50],
            [28, 30, 25, 50],
            [29, 31, 26, 50],
            [30, 50, 27, 50]
                        
            
        ]

        self.max_point = 32

        self.gem = []

        self.time_eat = pygame.time.get_ticks()


    def get_display(self):
        return self.maplvl1

    def create_gem(self):
        
        y = 50
        for x in range(50, 1750, 20):
            self.gem.append([x, y])


        y = 250
        for x in range(50, 450, 20):
            self.gem.append([x, y])

        y = 250
        for x in range(570, 1230, 20):
            self.gem.append([x, y])

        y = 250
        for x in range(1350, 1750, 20):
            self.gem.append([x, y])

        y = 450
        for x in range(50, 450, 20):
            self.gem.append([x, y])

        y = 450
        for x in range(570, 1230, 20):
            self.gem.append([x, y])

        y = 450
        for x in range(1350, 1750, 20):
            self.gem.append([x, y])


        y = 650
        for x in range(50, 1750, 20):
            self.gem.append([x, y])

        x = 50
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 450
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 570
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 785
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 1015
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 1230
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 1350
        for y in range(50, 650, 20):
            self.gem.append([x, y])

        x = 1750
        for y in range(50, 650, 20):
            self.gem.append([x, y])
     


        print(str(len(self.gem)) + " gems")


    def draw_gem(self, screen):
        for g in self.gem:
            screen.blit(self.gemsp, (g[0]-6, g[1]-6))

    def play_chomp(self):
        playsound("./sound/pacman_chomp.wav")
        
    def eat_gem(self, pac):

        dl = []
        ln = len(self.gem)
        for i in range(ln):
            if distance(self.gem[i][0], self.gem[i][1], pac.posX, pac.posY) <= 25:
                pac.score += 10
                dl.append(i)

        ln = len(dl)
        for i in range(ln-1, -1, -1):
            self.gem.pop(dl[i])

        if ln > 0:
            t = pygame.time.get_ticks() - self.time_eat
            if t >= 1000:
                t1 = threading.Thread(target=self.play_chomp)
                t1.start()
                self.time_eat = pygame.time.get_ticks()
            
        if len(self.gem) == 0:
             return 1

        return 0
        