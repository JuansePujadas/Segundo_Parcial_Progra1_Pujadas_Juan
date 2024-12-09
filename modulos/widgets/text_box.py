import pygame
from .widget import Widget
from ..variables import (COLOR_ANARANJADO, RUTA_FUENTE)

class TextBox(Widget):

    def __init__(self, x, y, texto, pantalla, font_size = 25, on_click = None, on_click_param = None):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pygame.font.Font(RUTA_FUENTE, self.font_size)
        self.image = self.font.render(self.texto, True, COLOR_ANARANJADO)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.on_click = on_click
        self.on_click_param = on_click_param

        self.write_on = True
        self.writing = ''
        self.image_write = self.font.render(self.writing, False, COLOR_ANARANJADO)
        self.rect_write = self.image_write.get_rect()
        self.rect_write.center = (x, y)
    
    def write_on_box(self, event_list: list):
        for evento in event_list:
            if evento.type == pygame.KEYDOWN and self.write_on:
                if evento.key == pygame.K_BACKSPACE:
                    self.writing = self.writing[:-1]
                else:
                    self.writing += evento.unicode

    def draw(self):
        super().draw()
        self.image.blit(self.pantalla, (self.rect_write.x, self.rect_write.y))

    def update(self, event_list: list):
        self.draw()
        self.write_on_box(event_list)