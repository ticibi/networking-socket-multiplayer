import pygame

from constants import Colors, WIDTH, HEIGHT, CELL


class Grid:
    def __init__(self):
        self.show_grid = True

    def toggle(self):
        self.show_grid = not self.show_grid

    def update(self, window):
        if not self.show_grid:
            return
        for x in range(0, WIDTH, CELL):
            for y in range(0, HEIGHT, CELL):
                rect = pygame.Rect(x, y, CELL, CELL)
                pygame.draw.rect(window, Colors.GRID, rect, 1)
