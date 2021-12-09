from collections import namedtuple
import pygame
from typing import Protocol
import sys

from constants import FPS, Colors, RES
from world import Grid


WINDOW = pygame.display.set_mode(RES)


class GameObject(Protocol):
    def update(self):
        """update the game object"""


class GameMode:
    def __init__(self):
        self.debug = False
        self.events = {}
        self.objects: list[GameObject] = []

    def initialize(self):
        self.create_event(tag='collision', time=FPS)
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.objects.append(self.grid)

    def connect(self, network_class):
        if not network_class:
            return
        self.network = network_class
        try:
            self.network._connect()
        except ConnectionRefusedError:
            print('failed to connect')

    def _update(self, window, func):
        self.clock.tick(FPS)
        window.fill(Colors.BLACK)
        for obj in self.objects:
            obj.update(window)
        if func:
            func()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == self.events['collision'].event:
                pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_b:
                    pass
                if event.key == pygame.K_g:
                    self.grid.toggle()
                if event.key == pygame.K_i:
                    pass
                if event.key == pygame.K_x:
                    pass

    def create_event(self, tag:str, time:int):
        i = len(self.events) + 1
        user_event = pygame.USEREVENT + i
        event = namedtuple(tag, 'event time')
        self.events[tag] = event(user_event, time)
        pygame.time.set_timer(user_event, time)

    def run(self, func=None):
        while True:
            self._handle_events()
            self._update(WINDOW, func)
            pygame.display.update()
