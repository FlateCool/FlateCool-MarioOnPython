import pygame
from settings import *
from world import *
from player import *
from camera import *

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Super Mario Boy")
bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
bg.fill(BACKGROUND_COLOR)

hero = Player(55, 55, screen)
camera = Camera()
world = World(screen, camera, level, hero)
world.load_world()
timer = pygame.time.Clock()



def main():
    isRunning = True
    while isRunning:
        screen.blit(bg, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                isRunning = False

        world.render()
        hero.movement(world.platforms)
        pygame.display.update()
        timer.tick(60)

    pygame.quit()
    exit()




if __name__ == "__main__":
    main()
