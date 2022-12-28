import pygame
from settings import *
import pyganim


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image, block_type='pf'):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.deleted = False
        self.x = x
        self.y = y
        self. type = block_type
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Coin(Platform):
    def __init__(self, x, y, block_type='coin'):
        image = pygame.image.load('mario/coin.png')
        Platform.__init__(self, x, y, image, block_type)
        self.cost = 1


class Teleport(pygame.sprite.Sprite):
    def __init__(self, x, y, goX, goY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.x = x
        self.y = y
        self.goX = goX
        self.goY = goY
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.image.set_colorkey(WHITE)  # делаем фон прозрачным
        self.animObj = pyganim.PygAnimation([('blocks/portal1.png', 100), ('blocks/portal2.png', 100)])
        self.animObj.play()

    def animate(self):
        self.animObj.play()
        self.image.fill(WHITE)
        self.animObj.blit(self.image, (0, 0))

    def handler(self, player):
        if pygame.sprite.collide_rect(self, player):  # если есть пересечение платформы с игроком
            player.rect.x = int(self.goX)
            player.rect.y = int(self.goY)

















