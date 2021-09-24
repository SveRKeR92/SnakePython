import pygame

class Grid:
      def __init__(self, screenWidth, screenHeight, ecran):
            self.ecran = ecran
            self.tableSize = 25
            self.tableGridWidth = screenWidth / self.tableSize
            self.tableGridHeight = screenHeight / self.tableSize

      def displayGrid(self, color):
            for x in range(0, int(self.tableGridWidth)):
                  for y in range(0, int(self.tableGridHeight)):
                        pygame.draw.rect(self.ecran, color, (x*self.tableSize, y*self.tableSize, self.tableSize-1, self.tableSize-1))