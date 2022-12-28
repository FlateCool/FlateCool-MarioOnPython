import pygame
from pytmx.util_pygame import load_pygame
from settings import *

class Loader(object):
    def __init__(self, maptmxfilepath, pathtotiles):
        self.gameMap = load_pygame(maptmxfilepath)
        self.Layers = list(self.gameMap.visible_layers)
        self.tiles = pygame.image.load(pathtotiles).convert()

    def get_Background(self):
        Background = self.Layers[0]
        return Background

    def get_Platforms(self):
        Platforms = self.Layers[1]
        return Platforms

    def get_Teleports(self):
        Teleports = self.gameMap.get_layer_by_name("Teleports")
        return Teleports

    def get_Coins(self):
        Coins = self.gameMap.get_layer_by_name("Coins")
        return Coins

    def get_tile_image(self, x, y, layer):
        im = self.gameMap.get_tile_image(x, y, layer)
        return im

    def get_player_coordinates(self):
        player = self.gameMap.get_object_by_name("Player")
        return (player.x, player.y)

    def get_level_size(self):
        return (self.gameMap.width, self.gameMap.height)