import pygame
from level import *
from settings import *
from blocks import *


class World(object):
    def __init__(self, surface, camera, level, player):
        self.level = level
        self.surface = surface
        self.camera = camera
        self.player = player
        self.entities = pygame.sprite.Group()  # Все объекты
        self.platforms = []  # то, во что мы будем врезаться или опираться
        self.entities.add(self.player)

    def load_world(self):

        x = y = 0  # координаты
        for row in self.level:
            for col in row:
                if col == "-":
                    pf = Platform(x, y)
                    self.entities.add(pf)
                    self.platforms.append(pf)

                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

    def render(self):
        self.camera.update(self.player) # центризируем камеру относительно персонажа
        for e in self.entities:
            self.surface.blit(e.image, self.camera.apply(e))
