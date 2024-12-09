import pygame
from .widget import Widget
from ..variables import (COLOR_ANARANJADO, RUTA_FUENTE)

class TextTitle(Widget):

    def __init__(self, x, y, texto, pantalla, font_size=25):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pygame.font.Font(RUTA_FUENTE, self.font_size)
        self.image = self.font.render(self.texto, True, COLOR_ANARANJADO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.image = self.font.render(self.texto, True, COLOR_ANARANJADO)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.draw()