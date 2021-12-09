import pygame

from constants import CELL, FPS, HEIGHT, WIDTH, Colors
from utils import random_pos


class Player:
    def __init__(self, name):
        self.name = name
        self.pos = random_pos()
        self.last_pos = self.pos
        self.size = (CELL, CELL)
        self.rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.color = Colors.BLUE
        self.v = FPS
        self.moves = 0
        self.score = 0

    def update(self, window):
        self.move()
        self._update_rect()
        self._draw(window)

    def update_pos(self, pos):
        self.last_pos = self.pos
        self.pos = pos

    def _update_rect(self):
        self.rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])

    def _draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        enable_bounds = True
        x, y, v = self.pos[0], self.pos[1], self.v
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y -= v
        if keys[pygame.K_s]:
            y += v
        if keys[pygame.K_a]:
            x -= v
        if keys[pygame.K_d]:
            x += v
        # decide behavior when player moves to edge of screen
        if x < 0:
            x = 0 if enable_bounds else WIDTH - CELL
        if x > WIDTH - CELL:
            x = WIDTH - CELL if enable_bounds else 0
        if y < 0:
            y = 0 if enable_bounds else HEIGHT - CELL
        if y > HEIGHT - CELL:
            y = HEIGHT - CELL if enable_bounds else 0
        self.update_pos((x, y))
