import pygame
from .form import Form
from ..widgets import (Button, TextTitle)
from ..variables import (DIMENSION_PANTALLA, RUTA_FONDO_MAIN_MENU)

class FormMainMenu(Form):
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        #self.start_level = False

        self.music_update()
        
        self.surface = pygame.image.load(RUTA_FONDO_MAIN_MENU).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.main_menu_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-190, texto='This or That', pantalla=pantalla, font_size=95)
        self.main_menu_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-100, texto='MAIN MENU', pantalla=pantalla, font_size=45)

        self.button_start = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+20, texto='START', font_size=35, pantalla=pantalla, on_click=self.click_start, on_click_param='form_game')
        self.button_ranking = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+100, texto='RANKING', font_size=35, pantalla=pantalla, on_click=self.click_ranking, on_click_param='form_ranking')
        self.button_exit = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+180, texto='EXIT', font_size=35, pantalla=pantalla, on_click=self.click_exit)

        self.widget_list = [
            self.main_menu_subtitle, self.main_menu_title, self.button_exit, self.button_ranking, self.button_start
        ]

    def click_start(self, form_a_inicializar):
        #self.start_level = True
        self.set_active(form_a_inicializar)

    def click_ranking(self, form_a_inicializar):
        self.set_active(form_a_inicializar)

    def click_exit(self, form_a_inicializar):
        self.set_active(form_a_inicializar)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()

    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()