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


def main():
    run = True
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((800, 600))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
