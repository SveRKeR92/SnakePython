from random import randint
import pygame
from pygame.font import SysFont
from Player import Player
from Fruit import Fruit
from Grid import Grid

# # Vérifie si tous les modules sont chargés
module_charge = pygame.init();
# print(module_charge);
# Création fenêtre
# Plein écran
# ecran = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
# Petit ecran

screenHeight = 500
screenWidth = 500

randomColors = (randint(0, 255), randint(0, 255), randint(0, 255))

ecran = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption("Snake")
dir(ecran)

player = Player(ecran)
fruit = Fruit(ecran, screenWidth, screenHeight)
grid = Grid(screenWidth, screenHeight, ecran)

timer = pygame.time.Clock()

font = pygame.font.get_default_font()


# Boucle de jeu
loop = True


while loop:
    # ecran.blit(image, (250, 250))
    # pygame event
    timer.tick(10)
    ecran.fill((194, 194, 194))
    scoreDisplay = font.render('Score : '+ player.score, True, (0,0,0))

    grid.displayGrid(randomColors)

    player.displayPlayer()
    fruit.displayFruit()

    player.move(screenHeight, screenWidth)
    for event in pygame.event.get():
        # Event input keyboard
        if event.type == pygame.KEYDOWN:
            player.changeDirection(event.key)
            if event.key == pygame.K_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False

    
    if (player.getHeadPosition()) == (fruit.x, fruit.y):
        player.score += 1
        player.length += 1
        print("score : " + str(player.score))
        fruit = Fruit(ecran, screenWidth, screenHeight)


    # Affichage ecran
    pygame.display.flip()

# Vide le cache
pygame.quit()
