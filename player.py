import pygame
import pyganim
from settings import *


# pygame.time.get_ticks() - таймер

class Player(pygame.sprite.Sprite):
    def __init__(self, game, surface, loader):
        pygame.sprite.Sprite.__init__(self)
        x, y = loader.get_player_coordinates()
        self.loader = loader
        self.game = game
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = True  # На земле ли я?
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((MARIO_WIDTH, MARIO_HEIGHT))
        self.image.fill(GREEN)
        self.rect = pygame.Rect(x, y, MARIO_WIDTH, MARIO_HEIGHT)  # прямоугольный объект
        self.surface = surface
        self.money = 0
        self.max_lives = 3
        self.lives = self.max_lives
        
        # Подгружаем звуковые ресурсы
        self.sound_jump = pygame.mixer.Sound('Sounds/jump.mp3')
        self.sound_hurt = pygame.mixer.Sound('Sounds/sound_hurt.mp3')
        self.sound_coin = pygame.mixer.Sound('Sounds/coin.mp3')
        # Блокировщик звука прыжка
        self.sound_jump_blocker = False
        
        
        ''' Heroe's states: {Alive|Hurt|DEAD}
            Transitions:
            Alive <-> Hurt
            Dead <- Hurt
            Alive <-> Dead        
        '''
        # Начальное состояние 
        self.state = 'Alive'
        # Таймер для отсчета пребывания в состоянии 'Hurt'
        self.hurt_timer = 0
        # Время бессмертия (мс)
        self.time_for_immortary = 1000

        # animation initialization
        self.ANIMATION_DELAY = 100  # скорость смены кадров
        self.ANIMATION_RIGHT = [
            ('mario/r1.png'),
            ('mario/r2.png'),
            ('mario/r3.png'),
            ('mario/r4.png'),
            ('mario/r5.png')
        ]
        self.ANIMATION_LEFT = [
            ('mario/l1.png'),
            ('mario/l2.png'),
            ('mario/l3.png'),
            ('mario/l4.png'),
            ('mario/l5.png')
        ]
        self.ANIMATION_JUMP_LEFT = [('mario/jl.png', 100)]
        self.ANIMATION_JUMP_RIGHT = [('mario/jr.png', 100)]
        self.ANIMATION_JUMP = [('mario/j.png', 100)]
        self.ANIMATION_STAY = [('mario/0.png', 100)]

        self.image.set_colorkey(WHITE)  # делаем фон прозрачным
        #        Анимация движения вправо
        self.boltAnim = []
        for anim in self.ANIMATION_RIGHT:
            self.boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(self.boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        self.boltAnim = []
        for anim in self.ANIMATION_LEFT:
            self.boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(self.boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(self.ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(self.ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(self.ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(self.ANIMATION_JUMP)
        self.boltAnimJump.play()



    def toggle_state(self, to_state):
        if self.state == 'Alive' and to_state == 'Hurt':
            self.hurt_timer = pygame.time.get_ticks()
            self.lives -= 1
            self.state = 'Hurt'
            self.sound_hurt.play()
        elif self.state == 'Hurt' and to_state == 'Hurt':
            if pygame.time.get_ticks() - self.hurt_timer > self.time_for_immortary:
                self.state = 'Alive'
        


    def update(self, left, right, up, platforms):
        if self.state == 'DEAD':
            self.rect.x = self.startX
            self.rect.y = self.startY
            self.lives = self.max_lives
            self.state = 'Alive'
        elif self.state == 'Hurt':
            if self.lives <= 0:
                self.state = 'DEAD' 
                
        
                
        if self.state == 'Alive' or self.state == 'Hurt':   
        
            if up:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(WHITE)
                self.boltAnimJump.blit(self.image, (0, 0))
                if not self.sound_jump_blocker:
                    self.sound_jump.play()
                    self.sound_jump_blocker = True

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(WHITE)
                if up:  # для прыжка влево есть отдельная анимация
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
                else:
                    self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(WHITE)
                if up:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimRight.blit(self.image, (0, 0))


            if not (left or right):  # стоим, когда нет указаний идти
                self.xvel = 0
                if not up:
                    self.image.fill(WHITE)
                    self.boltAnimStay.blit(self.image, (0, 0))

            if not self.onGround:
                self.yvel += GRAVITY              
                if self.rect.y > self.loader.get_level_size()[1] * PLATFORM_HEIGHT:
                    self.state = 'DEAD'
                    self.sound_hurt.play()

            self.onGround = False  # Мы не знаем, когда мы на земле((

            self.rect.y += self.yvel
            self.collide(0, self.yvel, platforms)

            self.rect.x += self.xvel  # переносим свои положение на xvel
            self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if p.type == 'coin':
                    self.money += p.cost
                    p.cost = 0
                    p.deleted = True

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает
                    self.sound_jump_blocker = False

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def movement(self, platforms):

        left = right = False
        up = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True

        if keys[pygame.K_RIGHT]:
            right = True
            
        if keys[pygame.K_ESCAPE]:
            self.game.toggle()

        self.update(left, right, up, platforms)  # передвижение
