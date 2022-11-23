import pygame
import pytmx

class Loader(object):
    def __init__(self, maptmxfilepath):
        gameMap = pytmx.TiledMap(maptmxfilepath)
        Layers = list(gameMap.visible_layers)
        Background = Layers[0]
        Platforms = Layers[1]
        DieBlocks = Layers[2]
        Monsters = Layers[3]

        princess = gameMap.get_object_by_name('Princess')
        print(princess.x)
        for tile in Background:
            x, y, gid = tile
            im = gameMap.get_tile_image_by_gid(gid)
            #print(type(im))


bootloader = Loader('levels/map_1.tmx')