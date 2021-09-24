from math import pi
import math
import pygame
import random

class Fruit:
      def __init__(self, ecran, screenWidth, screenHeight):
            self.ecran = ecran
            self.width = 25
            self.color = (255, 0, 0)
            self.x = random.randrange(0, screenWidth, 25)
            self.y = random.randrange(0, screenHeight, 25)


      def displayFruit(self):
            pygame.draw.rect(self.ecran, self.color, pygame.Rect(self.x, self.y, self.width-1, self.width-1))
            
