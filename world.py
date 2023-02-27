import pygame
from settings import *
from blocks import *
from pytmx.util_pygame import load_pygame
from loader import *
from player import *
from effects import *


class World(object):
    def __init__(self, surface, camera, bootloader, game):
        self.surface = surface
        self.camera = camera
        self.bootloader = bootloader
        self.game = game
        self.player = Player(self.game, self.surface, self.bootloader)
        self.entity_player = pygame.sprite.Group()
        self.entity_player.add(self.player)
        self.entities = pygame.sprite.Group()  # Все объекты
        self.platforms = pygame.sprite.Group()  # то, во что мы будем врезаться или опираться
        self.handler_funcs = []
        self.animates_funcs = []
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        

        self.heart_image = pygame.image.load('mario/heart.png')
        self.coin_image = pygame.image.load('mario/coin.png')
        #self.effect = TeleportationEffect(self.player.rect.x, self.player.rect.y, self.surface)
        #self.effects = pygame.sprite.Group(self.effect)


    def draw_statistics(self):
        self.surface.blit(self.heart_image, (WIN_WIDTH - 170, 10))
        player_lives = self.font.render('x {}'.format(self.player.lives), True, BLACK)
        self.surface.blit(player_lives, (WIN_WIDTH - 130, 15))
        self.surface.blit(self.coin_image, (WIN_WIDTH - 80, 10))
        self.coin_statistics = self.font.render('x {}'.format(self.player.money), True, BLACK)
        self.surface.blit(self.coin_statistics, (WIN_WIDTH - 40, 15))

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
            self.platforms.add(pf)

        for teleport in self.bootloader.get_Teleports():
            ob = self.bootloader.gameMap.get_object_by_id(teleport.id)
            x = ob.x
            y = ob.y
            
            goX = teleport.properties['goX']
            goY = teleport.properties['goY']

            pf = Teleport(x, y, goX, goY)
            self.entities.add(pf)
            self.handler_funcs.append(pf.handler)
            self.animates_funcs.append(pf.animate)

            #self.handler_funcs.append(self.effect.handler)
            #self.animates_funcs.append(self.effect.animate)
            
            
        for die_block in self.bootloader.get_Die_Blocks():
            ob = self.bootloader.gameMap.get_object_by_id(die_block.id)
            x = ob.x
            y = ob.y           
            pf = Die_Block(x, y)
            self.entities.add(pf)
            #self.platforms.add(pf)
            self.handler_funcs.append(pf.handler)
            self.animates_funcs.append(pf.animate)
            
        for die_fire in self.bootloader.get_Die_Fires():
            ob = self.bootloader.gameMap.get_object_by_id(die_fire.id)
            x = ob.x
            y = ob.y 
            direction_x = int(ob.direction_x)         
                    
            pf = Die_Fire(x, y, direction_x)
            self.entities.add(pf)
            #self.platforms.add(pf)
            self.handler_funcs.append(pf.handler)
            self.animates_funcs.append(pf.animate)
            

        for coin in self.bootloader.get_Coins():
            ob = self.bootloader.gameMap.get_object_by_id(coin.id)
            x = ob.x
            y = ob.y
            
            #goX = coin.properties['goX']
            #goY = teleport.properties['goY']

            pf = Coin(x, y, 'coin')
            self.entities.add(pf)
            self.platforms.add(pf)


            #self.handler_funcs.append(self.effect.handler)
            #self.animates_funcs.append(self.effect.animate)


    def render(self):
        self.camera.update(self.player)  # центризируем камеру относительно персонажа
        for e in self.entities:

            if isinstance(e, Coin) and e.deleted:
                self.player.money += e.cost
                self.entities.remove(e)
                self.platforms.remove(e)
                self.player.sound_coin.play()


            self.surface.blit(e.image, self.camera.apply(e))

        for e in self.entity_player:
            self.surface.blit(e.image,  self.camera.apply(e))

        self.player.movement(self.platforms)
        self.process_handlers()
        self.process_animate()
        self.draw_statistics()





    def process_handlers(self):
        for h in self.handler_funcs:
            h(self.player)

    def process_animate(self):
        for h in self.animates_funcs:
            h()





