import pygame
from settings import *
from blocks import *
from pytmx.util_pygame import load_pygame
from loader import *
from player import *


class World(object):
    def __init__(self, surface, camera, bootloader):
        self.surface = surface
        self.camera = camera
        self.bootloader = bootloader
        self.player = Player(self.surface, self.bootloader)
        self.entity_player = pygame.sprite.Group()
        self.entity_player.add(self.player)
        self.entities = pygame.sprite.Group()  # Все объекты
        self.platforms = []  # то, во что мы будем врезаться или опираться


    def load_world(self):
        for tile in self.bootloader.get_Background().tiles():
            x, y, gid = tile
            im = self.bootloader.get_tile_image(x, y, LBackground)
            pf = Platform(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT, im)
            self.entities.add(pf)


        for tile in self.bootloader.get_Platforms().tiles():
            x, y, gid = tile
            im = self.bootloader.get_tile_image(x, y, LPlatforms)
            pf = Platform(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT, im)

            self.entities.add(pf)
            self.platforms.append(pf)



    def render(self):
        self.camera.update(self.player)  # центризируем камеру относительно персонажа
        for e in self.entities:
            self.surface.blit(e.image, self.camera.apply(e))
        for e in self.entity_player:
            self.surface.blit(e.image,  self.camera.apply(e))
