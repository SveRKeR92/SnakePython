import pygame
import random
from Directions import *
from Grid import Grid

ecran = pygame.display.set_mode((650, 650))

directions = Directions()
grid = Grid(999, 999, ecran)

right = directions.right
left = directions.left
up = directions.up
down = directions.down

class Player:
    def __init__(self, ecran):
        self.ecran = ecran
        self.positions = [(250, 250)]
        self.width = 25
        self.length = 1
        self.score = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.direction = random.choice([right, left, up, down])

    def getHeadPosition(self):
        headPos = self.positions[0]
        return headPos

    def move(self, screenHeight, screenWidth):
        head = self.getHeadPosition()
        headX = head[0]
        headY = head[1]
        moveX = self.direction[0]
        moveY = self.direction[1]

        if headX + moveX * grid.tableSize  < 0:
            headX = screenWidth
        if headX + moveX * grid.tableSize > screenWidth - self.width:
            headX = -self.width
        if headY + moveY*grid.tableSize < 0:
            headY = screenHeight
        if headY + moveY*grid.tableSize > screenHeight - self.width:
            headY = -self.width

        newPos = ((headX + moveX * grid.tableSize), (headY + moveY*grid.tableSize))

        # check if player is touching himself, starting at 3 length
        if len(self.positions) > 2 and newPos in self.positions[2:]:
            self.__init__(self.ecran) # Reset Player
        else: # if not touching, insert new Pos as the head
            self.positions.insert(0, newPos)
            if len(self.positions) > self.length: # if number of pos > snake length, cut the old pos
                self.positions.pop()

        
        #self.positions[0] = taillecase * head

    def changeDirection(self, eventKeyboard):
        if eventKeyboard == pygame.K_LEFT or eventKeyboard == pygame.K_q :
            self.direction = left
        if eventKeyboard == pygame.K_RIGHT or eventKeyboard == pygame.K_d:
            self.direction = right
        if eventKeyboard == pygame.K_UP or eventKeyboard == pygame.K_z:
           self.direction = up
        if eventKeyboard == pygame.K_DOWN or eventKeyboard == pygame.K_s:
            self.direction = down

    def displayPlayer(self):
        for pos in self.positions:
            pygame.draw.rect(self.ecran, self.color, pygame.Rect(pos[0], pos[1], self.width-1, self.width-1))


