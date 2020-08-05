# GUI using pygame

# Imports

import pygame
# import json
# import os
from pygame.locals import *

pygame.font.init()

# Variables

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GREY = (198, 214, 198)

SEA_GREEN = (0,255,197)

BLOCK_FONT = pygame.font.SysFont("lemon", 20)
OPTION_FONT = pygame.font.SysFont("lemon", 13)


class Block:
    def __init__(self, x, y, colour, name, func=None):
        self.color = colour
        self.x = x
        self.y = y
        self.w = 200
        self.h = 50

        self.func = func

        self.text = BLOCK_FONT.render(name, True, BLACK)
        self.text_input = TextInput(self.x + self.w - 85, self.y + self.h - 45,
                                    80, 40)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))
        self.text_input.draw(win)
        win.blit(self.text, (self.x + 4, self.y + 4))


class FunctionOptions:
    def __init__(self, x, y, colour, name):
        self.colour = colour
        self.x = x
        self.y = y
        self.w = 120
        self.h = 30

        self.text = OPTION_FONT.render(name, True, BLACK)
        self.text_input = TextInput(self.x + self.w - 85, self.y + self.h - 45, 80, 40)

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))
        win.blit(self.text, (self.x + 4, self.y + 4))


class TextInput:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.h))


class Tree:
    def __init__(self):
        self.blocks = []
        self.len = len(self.blocks)

    def append(self, block):
        self.blocks.append(block)
        self.len = len(self.blocks)

    def remove(self, block):
        self.blocks.remove(block)
        self.len = len(self.blocks)


def main():
    def draw():
        win.fill(GREY)

        # TEST
        pygame.draw.circle(win, RED, (width // 2, height // 2), 10)
        # print(option)
        if option == 0:
            for b in bif.blocks:
                b.draw(win)
        elif option == 1:
            for b in ope.blocks:
                b.draw(win)
        for b in options.blocks:
            b.draw(win)

        pygame.display.update()

    width, height = 1000, 600

    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((width, height), flags=RESIZABLE)
    pygame.display.set_caption("Code generator")

    bif = Tree()

    bif.append(Block(50, 100, GREEN, "output", "print"))

    ope = Tree()
    ope.append(Block(50, 100, RED, "sum", "sum"))

    options = Tree()

    options.append(FunctionOptions(40, 25, SEA_GREEN, "built-in-func"))
    options.append(FunctionOptions(180, 25, SEA_GREEN, "operators"))

    option = 0
    while run:
        clock.tick(FPS)
        draw()

        mx, my = pygame.mouse.get_pos()
        if 170 > mx > 50 > my > 25 and pygame.mouse.get_pressed()[0]:
            option = 0

        if 200 < mx < 320 and 25 < my < 50 and pygame.mouse.get_pressed()[0]:
            option = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                win = pygame.display.set_mode((width, height), flags=RESIZABLE)

    pygame.quit()


main()
