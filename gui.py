# GUI using pygame

# Imports
import json

import pygame
# import os
from pygame.locals import *

import compiler

pygame.font.init()

# Variables

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GREY = (198, 214, 198)

SEA_GREEN = (0, 255, 197)

BLOCK_FONT = pygame.font.SysFont("lemon", 20)
OPTION_FONT = pygame.font.SysFont("lemon", 13)


class Block:
    def __init__(self, x, y, colour, name, func=None):
        self.color = colour
        self.x = x
        self.y = y
        self.w = 200
        self.h = 50
        self.name = name
        self.func = func

        self.text = BLOCK_FONT.render(name, True, BLACK)
        self.text_input = TextInput(self.x + self.w - 85, self.y + self.h - 45, 80, 40)

    def draw(self, win, x, y):
        pygame.draw.rect(win, self.color, (x, y, self.w, self.h))
        self.text_input.draw(win)
        win.blit(self.text, (self.x + 4, self.y + 4))

    def moving(self, win, x, y):
        pygame.draw.rect(win, self.color, (x, y, self.w, self.h))
        self.text_input.moving(win, x + self.w - 85, y + self.h - 45)
        win.blit(self.text, (x + 4, y + 4))

    def clicked(self, pos):
        x, y = pos
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            return True
        return False


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

    def clicked(self, pos):
        x, y = pos
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            return True
        return False


class TextInput:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.h))

    def moving(self, win, x, y):
        pygame.draw.rect(win, WHITE, (x, y, self.w, self.h))


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

    def as_dict(self):
        d = {}
        for i, b in enumerate(self.blocks):
            d.update({f"{b.func}{i}": {"args": "'TEST', 'Another test'"}})

        return d


def main():
    def draw():
        win.fill(GREY)

        # TEST
        pygame.draw.circle(win, RED, (width // 2, height // 2), 10)

        if option == 0:
            for b in bif.blocks:
                b.draw(win, b.x, b.y)
        elif option == 1:
            for b in ope.blocks:
                b.draw(win, b.x, b.y)

        for b in options.blocks:
            b.draw(win)

        for b in code.blocks:
            b.draw(win, b.x, b.y)

        for b in moving.blocks:
            p_x, p_y = pygame.mouse.get_pos()
            b.moving(win, p_x, p_y)

        pygame.display.update()

    width, height = 1000, 600

    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((width, height), flags=RESIZABLE)
    pygame.display.set_caption("Code generator")

    bif = Tree()

    bif.append(Block(50, 100, GREEN, "output", "print"))

    ope = Tree()
    ope.append(Block(50, 100, RED, "sum", "comment"))  # testing

    options = Tree()

    options.append(FunctionOptions(40, 25, SEA_GREEN, "built-in-func"))
    options.append(FunctionOptions(180, 25, SEA_GREEN, "operators"))

    moving = Tree()
    code = Tree()

    option = 0
    flying = False

    while run:
        clock.tick(FPS)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                win = pygame.display.set_mode((width, height), flags=RESIZABLE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, o in enumerate(options.blocks):
                    if o.clicked((x, y)):
                        option = i
                        break
                # choosing blocks
                a = None
                if option == 0:
                    a = bif.blocks
                elif option == 1:
                    a = ope.blocks

                if not flying:
                    for i in a:
                        if i.clicked((x, y)):
                            moving.append(i)
                            flying = True
                else:
                    for i in moving.blocks:
                        code.append(Block(x, y, i.color, i.name, i.func))
                    moving = Tree()
                    flying = False

    with open("blocks.json", "w") as j:
        json.dump(code.as_dict(), j)
    with open("blocks.json", "r") as j:
        compiler.test_case(json.load(j))

    pygame.quit()


main()
