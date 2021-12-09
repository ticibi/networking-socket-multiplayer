import logging
import socket

import pygame

from constants import BUFFER, CELL, LOCALHOST, PORT, TITLE, Colors
from game import WINDOW, GameMode
from player import Player
from ui import UI
from utils import pos_to_str, str_to_pos

logging.basicConfig(level=logging.DEBUG)


class Client:
    def __init__(self, host, port):
        self.network_id = None
        self.name = input('enter username: ')
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connect(self):
        self.socket.connect((self.host, self.port))
        server_name = self.socket.send(self.name.encode())
        logging.debug(f'connected to {server_name}')

    def send(self, data: str):
        self.socket.send(data.encode())
        return self.socket.recv(BUFFER).decode()

class GameClient(GameMode):
    def __init__(self):
        super().__init__()
        self.connect(Client(LOCALHOST, PORT))
        self.player = Player(self.network.name)
        self.objects.append(self.player)
        self.ui = UI()
        self.objects.append(self.ui)

    def update(self):
        try:
            reply = self.network.send(pos_to_str(self.player.pos))
            print(reply)
            if reply:
                pos = str_to_pos(reply)
                rect = (pos[0], pos[1], CELL, CELL)
                pygame.draw.rect(WINDOW, Colors.PURPLE, rect)
        except:
            pass

    def __repr__(self):
        return '[client]'


if __name__ == "__main__":
    game = GameClient()
    pygame.display.set_caption(f'{game} {TITLE}')
    game.initialize()
    game.run(game.update)
