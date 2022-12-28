import pygame
import pyganim
from settings import *


class TeleportationEffect(pygame.sprite.Sprite):
    def __init__(self, x, y, surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(BACKGROUND_COLOR)
        self.rect = pygame.Rect(x, y, MARIO_WIDTH, MARIO_HEIGHT)  # прямоугольный объект
        self.surface = surface
        self.x = x
        self.y = y
        self.boltAnim = pyganim.PygAnimation([('mario/test.png', 100)])
        '''
        self.boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 100),
                                             ('testimages/bolt_strike_0002.png', 100),
                                             ('testimages/bolt_strike_0003.png', 100),
                                             ('testimages/bolt_strike_0004.png', 100),
                                             ('testimages/bolt_strike_0005.png', 100),
                                             ('testimages/bolt_strike_0006.png', 100),
                                             ('testimages/bolt_strike_0007.png', 100),
                                             ('testimages/bolt_strike_0008.png', 100),
                                             ('testimages/bolt_strike_0009.png', 100),
                                             ('testimages/bolt_strike_0010.png', 100)])

        '''
        

        self.duration = 1000

    def __del__(self):
        print('Delete teleportation effect')

    def animate(self):
        self.boltAnim.play()
        self.image.fill(BACKGROUND_COLOR)
        self.boltAnim.blit(self.image, (0, 0))

    def handler(self, player):
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        if self.duration:
            self.duration -= 1
            print("Уменьшаем", self.duration)
        else:
            del self

class Empty():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, MARIO_WIDTH, MARIO_HEIGHT)  # прямоугольный объект

