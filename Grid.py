import pygame
import random

class Grid:
      def __init__(self, screenWidth, screenHeight, ecran):
            self.ecran = ecran
            self.tableSize = 25
            self.tableGridWidth = screenWidth / self.tableSize
            self.tableGridHeight = screenHeight / self.tableSize
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

      def displayGrid(self):
            for x in range(0, int(self.tableGridWidth)):
                  for y in range(0, int(self.tableGridHeight)):
                        pygame.draw.rect(self.ecran, self.color, (x*self.tableSize, y*self.tableSize, self.tableSize-1, self.tableSize-1))

      def gridNewColor(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))