import pygame
import sys
import math
import heapq
import threading
from playsound import playsound
from ghost import *

def distance(x, y, x2, y2):
    return math.sqrt((x-x2)**2 + (y-y2)**2)

class Ennemy(Ghost):

    def __init__(self):

        Ghost.__init__(self)
          
        self.path = [13, 17, 18, 14]

        self.ind_path = 0
        self.start = 1

        self.time_move = pygame.time.get_ticks()
        self.detect_p = 0

    def update_pos(self, ml, freeze):
        next_point = (self.ind_path + 1) % len(self.path)
        

        if self.start:
            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

            if self.posX < ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 3
            elif self.posX > ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 2
            elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY < ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 1
            elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY > ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 0

            self.start = 0
                    

        if not freeze:
            t = pygame.time.get_ticks() - self.time_move
            if self.detect_p == 3:
                self.posX += t * 40.0 / 250.0
            elif self.detect_p == 2:
                self.posX -= t * 40.0 / 250.0
            elif self.detect_p == 1:
                self.posY += t * 40.0 / 250.0
            elif self.detect_p == 0:
                self.posY -= t * 40.0 / 250.0
                   
       
        if self.detect_p == 3 and self.posX >= ml.turn_point[self.path[next_point]][0]:
            self.ind_path = (self.ind_path + 1) % len(self.path)
            next_point = (self.ind_path + 1) % len(self.path)
            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        elif self.detect_p == 2 and self.posX <= ml.turn_point[self.path[next_point]][0]:
            self.ind_path = (self.ind_path + 1) % len(self.path)
            next_point = (self.ind_path + 1) % len(self.path)
            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        elif self.detect_p == 1 and self.posY >= ml.turn_point[self.path[next_point]][1]:
            self.ind_path = (self.ind_path + 1) % len(self.path)
            next_point = (self.ind_path + 1) % len(self.path)
            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        elif self.detect_p == 0 and self.posY <= ml.turn_point[self.path[next_point]][1]:
            self.ind_path = (self.ind_path + 1) % len(self.path)
            next_point = (self.ind_path + 1) % len(self.path)
            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]


        if self.posX < ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
            self.detect_p = 3
        elif self.posX > ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
            self.detect_p = 2
        elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY < ml.turn_point[self.path[next_point]][1]:
            self.detect_p = 1
        elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY > ml.turn_point[self.path[next_point]][1]:
            self.detect_p = 0
        
        self.time_move = pygame.time.get_ticks()

    def play_death(self):
        playsound("./sound/pacman_death.wav")

    def death_pac(self, pac):

        if distance(pac.posX, pac.posY, self.posX, self.posY) <= 25:
            pac.death = 1
            pac.life -= 1
            t1 = threading.Thread(target=self.play_death)
            t1.start()
            return 1

        return 0


def a_star(ml, start, end, cost_func):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == end:
            return path
        #for neighbor in graph[current]:
        for i in range(4):
            if ml.neigh[current][i] != 50:
                edge_cost = cost_func(ml.turn_point[current], ml.turn_point[ml.neigh[current][i]])
                heapq.heappush(heap, (cost + edge_cost, ml.neigh[current][i], path))
    return []

def manhattan_distance(current, neighbor):
    return abs(neighbor[0] - current[0]) + abs(neighbor[1] - current[1])

class EnnemyA(Ennemy):

    def __init__(self):
        Ennemy.__init__(self)

        self.time_change_path = pygame.time.get_ticks()
        self.statepath = 0
                
    def find_pac(self, ml, pac, now):
      
        t = pygame.time.get_ticks() - self.time_change_path
        if t >= 2000 or now:
                     
            pos_s = self.path[self.ind_path]
            ind = self.ind_path + 1
            if ind >= len(self.path):
                ind -= 1
            pos_n = self.path[ind]

            next_p = pac.next_point
            if next_p == 50 or pac.next_point == pos_n:
                next_p = pac.ind_point
            pa = a_star(ml, self.path[ind], next_p, manhattan_distance)
                       
            self.path = [pos_s] + pa
                              
            self.ind_path = 0
            
            self.time_change_path = pygame.time.get_ticks()


    def update_pos(self, ml, freeze):
        next_point = (self.ind_path + 1)
        
        if next_point >= len(self.path):
            return -1

        if self.start:
            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

            if self.posX < ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 3
            elif self.posX > ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 2
            elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY < ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 1
            elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY > ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 0

            
                    
        if not freeze:
            t = pygame.time.get_ticks() - self.time_move
            if self.detect_p == 3:
                self.posX += t * 40.0 / 250.0
            elif self.detect_p == 2:
                self.posX -= t * 40.0 / 250.0
            elif self.detect_p == 1:
                self.posY += t * 40.0 / 250.0
            elif self.detect_p == 0:
                self.posY -= t * 40.0 / 250.0
                   
       
        if self.detect_p == 3 and self.posX >= ml.turn_point[self.path[next_point]][0]:
        
            self.ind_path = (self.ind_path + 1) 
            next_point = (self.ind_path + 1) 
            if self.ind_path > len(self.path):
                self.ind_path = len(self.path)-1
                next_point = (self.ind_path + 1) 
           
            self.statepath = 1

            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        elif self.detect_p == 2 and self.posX <= ml.turn_point[self.path[next_point]][0]:
          
            self.ind_path = (self.ind_path + 1) 
            next_point = (self.ind_path + 1) 
            if self.ind_path > len(self.path):
                self.ind_path = len(self.path)-1
                next_point = (self.ind_path + 1) 
            
            self.statepath = 1

            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        elif self.detect_p == 1 and self.posY >= ml.turn_point[self.path[next_point]][1]:
       
            self.ind_path = (self.ind_path + 1) 
            next_point = (self.ind_path + 1) 
            if self.ind_path > len(self.path):
                self.ind_path = len(self.path)-1
                next_point = (self.ind_path + 1) 
          
            self.statepath = 1

            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        elif self.detect_p == 0 and self.posY <= ml.turn_point[self.path[next_point]][1]:
        
            self.ind_path = (self.ind_path + 1) 
            next_point = (self.ind_path + 1) 
            if self.ind_path > len(self.path):
                self.ind_path = len(self.path)-1
                next_point = (self.ind_path + 1) 
         
            self.statepath = 1

            self.posX = ml.turn_point[self.path[self.ind_path]][0]
            self.posY = ml.turn_point[self.path[self.ind_path]][1]

        if next_point < len(self.path):
            if self.posX < ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 3
            elif self.posX > ml.turn_point[self.path[next_point]][0] and self.posY == ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 2
            elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY < ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 1
            elif self.posX == ml.turn_point[self.path[next_point]][0] and self.posY > ml.turn_point[self.path[next_point]][1]:
                self.detect_p = 0
        
        self.time_move = pygame.time.get_ticks()

        self.start = 0

        return 1