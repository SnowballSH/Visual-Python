# GUI using pygame

# Imports

import pygame
import compiler

# use modules from compiler so it doesn't need to be imported again
json = compiler.json
os = compiler.os

os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (80, 80)

# Variables

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def draw(win):
    win.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Code generator")

    while run:
        clock.tick(FPS)

        draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
