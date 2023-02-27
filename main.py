import pygame
from settings import *
from world import *
from player import *
from camera import *
from loader import *
from menu import *
from game import *



pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Super Mario Boy")
bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

game = Game()
menu = Menu(screen, game)


bootloader = Loader('levels/map_1.tmx', 'levels/tiles.png')
camera = Camera(bootloader)
world = World(screen, camera, bootloader, game)
world.load_world()
timer = pygame.time.Clock()

# Продгружаем звуковые ресурсы
pygame.mixer.music.load('Sounds/background.mp3')
pygame.mixer.music.play(-1)


GAME_STATES = {'DEAD' : 1, 'ALIVE' : 2, 'NEXT_LEVEL': 3}

def main():
    """Главный игровой цикл
    """
    isRunning = True
     
    # отрисовываем игру
    # пока не вышли из игры
    while not game.GameQuit:
        if game.CURRENT_STATES == 'Running':
            screen.blit(bg, (0, 0))
            bg.fill(BACKGROUND_COLOR)
            for e in pygame.event.get():
                # Выходим из игры
                if e.type == pygame.QUIT:
                    game.GameQuit = True

            world.render()
            
            pygame.display.update()
            timer.tick(60)
        else:
            bg.fill(BLACK)  
            screen.blit(bg, (0, 0))             
            for e in pygame.event.get():
                # Выходим из игры
                if e.type == pygame.QUIT:
                    game.GameQuit = True 
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        menu.previous()
                    elif e.key == pygame.K_DOWN:
                        menu.next()
                    elif e.key == pygame.K_RETURN:
                        menu.submenu = True
                        menu.enter() 
                    elif e.key == pygame.K_ESCAPE and menu.submenu:
                        menu.submenu = False
                                  
            menu.draw()
            pygame.display.update()
            timer.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()