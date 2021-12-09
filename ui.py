import pygame

from constants import CELL, Colors


class Label:
    DEFAULT_FONT = 'resources/freesansbold.ttf'
    def __init__(self, tag: str, text: str, pos: tuple, size: int, color: tuple, visible: bool):
        self.tag = tag
        self.pos = pos
        self.text = text
        self.size = size
        self.color = color
        self.inactive_color = Colors.DARKGRAY
        self.base_color = color
        self.hover_color = Colors.GRAY
        self.visible = visible
        self.font = pygame.font.Font(
            Label.DEFAULT_FONT, 
            self.size
        )
    
    def update_text(self, text):
        self.text = text

    def draw(self):
        surface = self.font.render(
            f'{self.tag}: {self.text}', 
            1, 
            self.color
        )
        rect = surface.get_rect()
        rect.center = (
            self.pos[0] + self.size,
            self.pos[1] + self.size,
        )
        return surface, rect

    def render(self, window):
        if self.visible:
            surface, rect = self.draw()
            window.blit(surface, rect)


class UI:
    def __init__(self):
        self.elements = {}

    def create_label(self, tag, text, pos, size=CELL//2, color=Colors.CYAN, visible=True):
        label = Label(tag, text, pos, size, color, visible)
        self.elements[tag] = label

    def toggle_visibility(self):
        for element in self.elements.values():
            element.visible = not element.visible

    def _draw(self, window):
        for element in self.elements.values():
            element.render(window)
            
    def _mouse(self, window):
        pass

    def update(self, window):
        self._draw(window)
        self._mouse(window)