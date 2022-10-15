import pygame
from settings import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, type = 1):
        pygame.sprite.Sprite.__init__(self)
        if type == 1:
            self.image = pygame.image.load("blocks/platform.png")
        elif type == 2:
            self.image = pygame.image.load("blocks/Block.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
