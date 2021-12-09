import logging
import socket
import threading
import time

import pygame

from constants import BUFFER, LOCALHOST, PORT, TITLE
from game import GameMode

logging.basicConfig(level=logging.DEBUG)


class Server:
    def __init__(self, name: str, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.usernames = []
        self.client_data = []

    def _connect(self):
        """blinds socket and listens for new connections"""
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        logging.debug('[server] ONLINE')
        self._receive_connections()

    def _receive_connections(self):
        """accepts new connections"""
        while True:
            conn, addr = self.socket.accept()
            username = self.send(conn, self.name)
            time.sleep(2)
            self.clients.append(conn)
            self.client_data.append('')
            self.usernames.append(username)
            logging.debug(f'received connection from {conn}')
            logging.debug(f'{username} connected')
            thread = threading.Thread(target=self._client_connection, args=(conn,))
            thread.start()

    def _client_connection(self, conn):
        """handles each client connection"""
        while True:
            try:
                reply = conn.recv(BUFFER).decode()

                if reply.startswith('p'):
                    self.broadcast(conn, reply.encode())
                    logging.debug(f'broadcasting {reply}')
            except ConnectionError:
                index = self.clients.index(conn)
                username = self.usernames[index]
                self.usernames.remove(self.usernames[index])
                self.client_data.remove(self.client_data[index])
                self.clients.remove(conn)
                conn.close()
                logging.debug(f'{username} disconnected')
                break

    def send(self, conn, data):
        """send data and get a response"""
        conn.send(data.encode())
        return conn.recv(BUFFER).decode()

    def broadcast(self, conn, data):
        """send data to all clients"""
        for client in self.clients:
            if client != conn:
                client.send(data)


class GameServer(GameMode):
    def __init__(self):
        super().__init__()
        self.connect(Server('Cool Server', LOCALHOST, PORT))

    def __repr__(self):
        return '[server]'


if __name__ == "__main__":
    game = GameServer()
    pygame.display.set_caption(f'{game} {TITLE}')
    game.initialize()
    game.run()
