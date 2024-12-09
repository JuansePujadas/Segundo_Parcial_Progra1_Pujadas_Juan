import pygame
from .form import Form
from ..widgets import (Button, TextTitle)
from ..variables import (DIMENSION_PANTALLA, RUTA_FONDO_RANKING)
from ..auxiliar import cargar_ranking

class FormRanking(Form):

    def __init__(self, name, pantalla, x, y, active, level_num, music_path, ranking_list):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        self.surface = pygame.image.load(RUTA_FONDO_RANKING).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.confirm_name = True
        self.ranking_on_screen = []
        self.ranking_list = ranking_list

        self.ranking_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-230, texto='This or That', pantalla=pantalla, font_size=95)
        self.ranking_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-80, texto='LEDERBOARD', pantalla=pantalla, font_size=55)
        self.button_return_menu = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+250, texto='RETURN TO MAIN MENU', pantalla=pantalla, font_size= 45, on_click=self.click_return_menu, on_click_param='form_main_menu')

        self.init_ranking()

        self.widget_list = [
            self.ranking_title, self.ranking_subtitle, self.button_return_menu
        ]

    def cargar_ranking(self):
        self.ranking_list = cargar_ranking()
        self.init_ranking()

    def init_ranking(self):
        self.ranking_on_screen.clear()
        for i in range(len(self.ranking_list)):
            self.ranking_on_screen.append(
                TextTitle(x=DIMENSION_PANTALLA[0]//2-100, y=DIMENSION_PANTALLA[1]//2+i*25, texto=f'{i+1}', pantalla=self.pantalla)
            )
            self.ranking_on_screen.append(
                TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+i*25, texto=f'{self.ranking_list[i][0]}', pantalla=self.pantalla)
            )
            self.ranking_on_screen.append(
                TextTitle(x=DIMENSION_PANTALLA[0]//2+100, y=DIMENSION_PANTALLA[1]//2+i*25, texto=f'{self.ranking_list[i][1]}', pantalla=self.pantalla)
            )

    def click_return_menu(self, param):
        self.set_active(param)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        for ranking in self.ranking_on_screen:
            ranking.draw()

    def update(self):
        super().draw()
        for widget in self.widget_list:
            widget.update()