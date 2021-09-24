import pygame

class TextDisplay:
      def __init__(self, ecran, player, screenWidth, screenHeight) -> None:
          self.ecran = ecran
          self.player = player
          self.screenWidth = screenWidth
          self.screenHeight = screenHeight

      def displayScore(self):
        font = pygame.font.SysFont('Arial', 30)
        scoreDisplay = font.render('Score : '+ str(self.player.score), True, (0,0,0))
        speedDisplay = font.render('Speed : '+ str(self.player.speed), True, (0,0,0))
        controlsDisplay = font.render('Space to warp - C to change colors', True, (0, 0, 0))
        controlsRect = controlsDisplay.get_rect()
        controlsRect.center = (self.screenWidth // 2, self.screenHeight - 30)
        self.ecran.blit(scoreDisplay, (0, 0))
        self.ecran.blit(speedDisplay, (0, 30))
        self.ecran.blit(controlsDisplay, controlsRect)