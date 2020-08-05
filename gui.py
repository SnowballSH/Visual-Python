# GUI using pygame

# Imports

import pygame
import json
import os
from pygame.locals import *

pygame.font.init()

# Variables

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLOCK_FONT = pygame.font.SysFont("lemon", 25)


class Block:
    GAP = 20

    def __init__(self, x, y, color, name, func):
        self.color = color
        self.x = x
        self.y = y
        self.w = 200
        self.h = 50

        self.name = name
        self.func = func

        self.text = BLOCK_FONT.render(self.name, True, BLACK)
        self.text_input = TextInput(self.x + self.w - 85, self.y + self.h - 45,
                                    80, 40)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))
        self.text_input.draw(win)
        win.blit(self.text, (self.x + 4, self.y + 4))


class TextInput:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, win):
        pygame.draw.ellipse(win, WHITE, (self.x, self.y, self.w, self.h))


class Tree:
    def __init__(self):
        self.blocks = []
        self.len = len(self.blocks)

    def append(self, block: Block):
        self.blocks.append(block)
        self.len = len(self.blocks)

    def remove(self, block: Block):
        self.blocks.remove(block)
        self.len = len(self.blocks)


def main():
    def draw():
        win.fill(BLUE)

        # TEST
        pygame.draw.circle(win, RED, (width // 2, height // 2), 10)

        for b in tree.blocks:
            b.draw(win)

        pygame.display.update()

    width, height = 800, 600

    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((width, height), flags=RESIZABLE)
    pygame.display.set_caption("Code generator")

    tree = Tree()

    tree.append(Block(50, 50, GREEN, "output", "print"))
    tree.append(Block(50, 120, RED, "sum", "sum"))

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
