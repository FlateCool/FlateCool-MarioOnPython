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
        
class Die_Block(Platform):
    def __init__(self, x, y):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        Platform.__init__(self, x, y, self.image, 'Die_Block')
        
        self.image.set_colorkey(WHITE)  # делаем фон прозрачным
        self.animObj = pyganim.PygAnimation([
            ('blocks/dieBlock1.png', 50), ('blocks/dieBlock2.png', 50),
            ('blocks/dieBlock3.png', 50), ('blocks/dieBlock4.png', 50),
            ('blocks/dieBlock5.png', 50), ('blocks/dieBlock6.png', 50),
            ('blocks/dieBlock7.png', 50), ('blocks/dieBlock9.png', 50),
            ('blocks/dieBlock10.png', 50)
            ])
        self.animObj.play()
        
        
    def animate(self):    
        self.animObj.play()
        self.image.fill(WHITE)
        self.animObj.blit(self.image, (0, 0))
        

    def handler(self, player):
        if pygame.sprite.collide_rect(self, player):  # если есть пересечение платформы с игроком
            player.toggle_state('Hurt')           
            
            
class Die_Fire(Platform):
    def __init__(self, x, y, direction_x = 1):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        Platform.__init__(self, x, y, self.image, 'Die_Fire')
        
        # Количество спусков (подъёмов)
        self.count_x = 100
        self.count_y = 15
        
        self.trigger_x = 0
        self.trigger_y = 0
        # Направление движения
        self.direction_x = direction_x
        self.direction_y = 1 
        self.step_x = 2
        self.step_y = 2
        
         
            
        self.image.set_colorkey(WHITE)  # делаем фон прозрачным
        self.animObj = pyganim.PygAnimation([
            ('monsters/fire1.png', 300), ('monsters/fire2.png', 300)                
            ])
        self.animObj.play()
            
        
    def animate(self):            
        self.rect.x += self.direction_x * self.step_x
        self.rect.y += self.direction_y * self.step_y
        self.trigger_x += 1
        self.trigger_y += 1
        if not (self.trigger_x % self.count_x):
            self.direction_x *= -1
        if not (self.trigger_y % self.count_y):
            self.direction_y *= -1
        self.animObj.play()
        self.image.fill(WHITE)
        self.animObj.blit(self.image, (0, 0))
            

    def handler(self, player):
        if pygame.sprite.collide_rect(self, player):  # если есть пересечение платформы с игроком
            player.toggle_state('Hurt')
            


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
        self.animObj = pyganim.PygAnimation([('blocks/portal1.png', 500), ('blocks/portal2.png', 500)])
        self.animObj.play()

    def animate(self):
        self.animObj.play()
        self.image.fill(WHITE)
        self.animObj.blit(self.image, (0, 0))

    def handler(self, player):
        if pygame.sprite.collide_rect(self, player):  # если есть пересечение платформы с игроком
            player.rect.x = int(self.goX)
            player.rect.y = int(self.goY)

















