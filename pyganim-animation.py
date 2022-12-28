import sys
import os
sys.path.append(os.path.abspath('..'))

import pygame
from pygame.locals import *
import time
import pyganim
from effects import *
from player import *
from settings import *

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Pyganim Effects Demo')

teleportation_effect = TeleportationEffect(100, 100, windowSurface)


BGCOLOR = (100, 50, 50)

mainClock = pygame.time.Clock()


while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.blit(teleportation_effect.image, (teleportation_effect.x, teleportation_effect.y))
    teleportation_effect.handler(Empty(200, 100))
    teleportation_effect.animate()


    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.