from .widget import Widget
import pygame
from ..variables import (COLOR_ANARANJADO, RUTA_FUENTE, RUTA_SONIDO_BOTONES, COLOR_AZUL, COLOR_ROJO)

class Button(Widget):

    def __init__(self, x, y, texto, pantalla, font_size=25, on_click=None, on_click_param=None, cooldown_time=300, color=COLOR_ANARANJADO):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pygame.font.Font(RUTA_FUENTE, self.font_size)
        self.color = color
        self.image = self.font.render(self.texto, False, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.click_option_sfx = pygame.mixer.Sound(RUTA_SONIDO_BOTONES)
        self.on_click = on_click
        self.on_click_param = on_click_param
        
        self.cooldown_time = cooldown_time
        self.last_click_time = 0                                                        # Última vez que se hizo clic

    def button_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()

        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1:    # Comprobar si ha pasado suficiente tiempo desde el último clic
            if current_time - self.last_click_time > self.cooldown_time:
                self.last_click_time = current_time                                     # Actualizar el tiempo del último clic
                self.on_click(self.on_click_param)
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()

    def update(self):
        self.image = self.font.render(self.texto, False, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.button_pressed()
        self.draw()
