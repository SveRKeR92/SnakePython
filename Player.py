import pygame
import random
from Directions import *
from Grid import Grid
from  time import sleep

directions = Directions()

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
        self.speed = 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.direction = random.choice([right, left, up, down])
        self.grid = Grid(0, 0, ecran)

    def getHeadPosition(self):
        headPos = self.positions[0]
        return headPos

    def move(self, screenHeight, screenWidth):
        head = self.getHeadPosition()
        headX = head[0]
        headY = head[1]
        moveX = self.direction[0]
        moveY = self.direction[1]

        if headX + moveX * self.grid.tableSize  < 0:
            headX = screenWidth
        if headX + moveX * self.grid.tableSize > screenWidth - self.width:
            headX = -self.width
        if headY + moveY * self.grid.tableSize < 0:
            headY = screenHeight
        if headY + moveY * self.grid.tableSize > screenHeight - self.width:
            headY = -self.width

        newPos = ((headX + moveX * self.grid.tableSize), (headY + moveY * self.grid.tableSize))
       
        self.touchCheck(newPos)

    def touchCheck(self, newPos):
        # insert new Pos as the head 
        self.positions.insert(0, newPos) 
        # check if player is touching himself, starting at 3 length
        if len(self.positions) > 2 and newPos in self.positions[2:]:
            sleep(1)
            self.__init__(self.ecran) # Reset Player
        else: 
            if len(self.positions) > self.length: # cut the last pos if fruit not eaten
                self.positions.pop()


    def changeDirection(self, eventKeyboard):
        if (eventKeyboard == pygame.K_LEFT or eventKeyboard == pygame.K_q) and self.direction != right :
            self.direction = left
        if (eventKeyboard == pygame.K_RIGHT or eventKeyboard == pygame.K_d) and self.direction != left :
            self.direction = right
        if (eventKeyboard == pygame.K_UP or eventKeyboard == pygame.K_z) and self.direction != down :
           self.direction = up
        if (eventKeyboard == pygame.K_DOWN or eventKeyboard == pygame.K_s) and self.direction != up :
            self.direction = down

    def playerNewColor(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def displayPlayer(self):
        for pos in self.positions:
            pygame.draw.rect(self.ecran, self.color, pygame.Rect(pos[0], pos[1], self.width-1, self.width-1))



