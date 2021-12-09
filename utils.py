import json
import math
from random import randrange

from constants import WIDTH, HEIGHT, CELL


def read_json(filename):
    with open(f"{filename}.json", "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    return data

def write_json(data, filename):
    with open(f"{filename}.json", "w", encoding="utf-8-sig") as f:
        json.dump(data, f, indent=4)

def read_txt(filename):
    return open(filename + ".txt", "r").read()

def random_pos(max_x=WIDTH, max_y=HEIGHT, step=CELL) -> tuple:
    x = randrange(0, max_x, step)
    y = randrange(0, max_y, step)
    return (x, y)

def distance_to(pos1: tuple, pos2: tuple) -> float:
    '''returns magnitude of two tuple 2D vectors'''
    return math.sqrt(((pos2[0] - pos1[0])**2) + ((pos1[1] - pos2[1])**2))

def pos_to_str(pos):
    return f'p{pos[0]}:{pos[1]}'

def str_to_pos(str):
    str = str.replace('p', '', 1)
    str = str.split(':')
    return (int(str[0]), int(str[1]))
