import pygame
from settings import *
from world import *
from player import *
from camera import *
from loader import *

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Super Mario Boy")
bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
bg.fill(BACKGROUND_COLOR)

bootloader = Loader('levels/map_1.tmx', 'levels/tiles.png')
camera = Camera(bootloader)
world = World(screen, camera, bootloader)
world.load_world()
timer = pygame.time.Clock()

STATES = {'DEAD' : 1, 'ALIVE' : 2, 'NEXT_LEVEL': 3}

def main():
    isRunning = True
    while isRunning:
        screen.blit(bg, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                isRunning = False

        world.render()
        pygame.display.update()
        timer.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
