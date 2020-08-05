# GUI using pygame

# Imports

import pygame
import json
import os
from pygame.locals import *

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

class Block:
    IMG = "" #PLACEHOLDER HERE

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((800, 600),RESIZABLE)
    pygame.display.set_caption("Code generator")

    while run:
        clock.tick(FPS)
        draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                scrsize = event.size  # or event.w, event.h
                win = pygame.display.set_mode(scrsize, RESIZABLE)

    pygame.quit()


main()