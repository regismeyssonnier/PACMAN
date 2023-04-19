import pygame
import sys
import math

class Ghost:

    def __init__(self):

        self.w = 50
        self.h = 50

        self.ghostbel = pygame.image.load("img/ghostbel.png").convert_alpha()
        self.ghostber = pygame.image.load("img/ghostber.png").convert_alpha()

        self.ghostb = [self.ghostbel, self.ghostber]

        self.indghb = 0
        self.time_ghostb = pygame.time.get_ticks()

        self.posX = 900
        self.posY = 350

    def set_ghostb(self):
        self.indghb = (self.indghb + 1) % 2

    def get_ghostb(self):
        return self.ghostb[self.indghb]


    def draw(self, screen):
        t = pygame.time.get_ticks() - self.time_ghostb
        if t >= 250:
            self.set_ghostb()
            self.time_ghostb = pygame.time.get_ticks()
        screen.blit(self.get_ghostb(), (self.posX-25, self.posY-25)) 

      