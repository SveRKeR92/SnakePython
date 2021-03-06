from Directions import Directions
import random
import pygame
from pygame.font import SysFont
from Player import Player
from Fruit import Fruit
from Grid import Grid
from TextDisplay import TextDisplay

pygame.init()

screenHeight = 500
screenWidth = 500

ecran = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption("Snake")
dir(ecran)

player = Player(ecran)
fruit = Fruit(ecran, screenWidth, screenHeight)
grid = Grid(screenWidth, screenHeight, ecran)
directions = Directions()
text = TextDisplay(ecran, player, screenWidth, screenHeight)

timer = pygame.time.Clock()

# Boucle de jeu
loop = True

while loop:
    # ecran.blit(image, (250, 250))
    # pygame event
    timer.tick(player.speed)
    ecran.fill((194, 194, 194))

    grid.displayGrid()
    player.displayPlayer()
    fruit.displayFruit()
    text.displayScore()

    player.move(screenHeight, screenWidth)
    for event in pygame.event.get():
        # Event input keyboard
        if event.type == pygame.KEYDOWN:
            player.changeDirection(event.key)

            if event.key == pygame.K_SPACE:
                ableToWarp = False

                while ableToWarp == False:
                    newRandPosX = random.randrange(0, screenWidth, 25)
                    newRandPosY = random.randrange(0, screenHeight, 25)
                    newHeadPos = (newRandPosX, newRandPosY)
                    print (newRandPosX, newRandPosY)
                    Error = True
                    for pos in player.positions:
                        if (newRandPosX, newRandPosX) == (pos[0], pos[1]):
                            Error = False
                            blockPosError = (pos[0], pos[1])
                    
                    if Error == False:
                        print("Unable to warp at : ", blockPosError)
                    else:
                        ableToWarp = True
                        player.touchCheck(newHeadPos)
                        player.direction = random.choice([directions.right, directions.left, directions.up, directions.down])

            if event.key == pygame.K_c:
                player.playerNewColor()
                grid.gridNewColor()

            if event.key == pygame.K_ESCAPE:
                loop = False

        if event.type == pygame.QUIT:
            loop = False
    
    if (player.getHeadPosition()) == (fruit.x, fruit.y):
        player.score += 1
        player.length += 1
        if player.score % 3 == 0:
            player.speed += 1
        fruit = Fruit(ecran, screenWidth, screenHeight)

    # Affichage ecran
    pygame.display.flip()

# Vide le cache
pygame.quit()
