# GUI using pygame

# Imports

import pygame
import json
import os
from pygame.locals import *

# Variables

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Block:
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 50, 30))


def main():
    def draw():
        win.fill(BLUE)

        # TEST
        pygame.draw.circle(win, RED, (width // 2, height // 2), 10)

        for b in blocks:
            b.draw(win)

        pygame.display.update()

    width, height = 800, 600

    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((width, height), flags=RESIZABLE)
    pygame.display.set_caption("Code generator")

    blocks = [Block(50, 50, GREEN)]

    while run:
        clock.tick(FPS)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                win = pygame.display.set_mode((width, height), flags=RESIZABLE)

    pygame.quit()


main()
