import pygame
from .form import Form
from ..widgets import (Button, TextTitle, TextBox)
from ..variables import (DIMENSION_PANTALLA, RUTA_FONDO_ENTER_NAME)
from ..logica import Logic

class FormEnterName(Form):
    def __init__(self, name, pantalla, x, y, active, level_num, music_path, score: int):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        self.surface = pygame.image.load(RUTA_FONDO_ENTER_NAME).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.score = score

        self.confirm_name = False

        self.enter_name_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-265, texto='GAME OVER', pantalla=pantalla, font_size=75)
        self.enter_name_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-80, texto='PLAYER NAME', pantalla=pantalla, font_size=35)
        self.score_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+80, texto=f'SCORE: {score}', pantalla=pantalla, font_size=45 )

        self.text_box = TextBox(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-35, texto='_____________', pantalla=pantalla)
        self.confirmation_button = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+210, texto='CONFIRM', pantalla=pantalla, font_size= 35, on_click=self.click_confirm_name)
        self.button_return_menu = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+270, texto='RETURN TO MAIN MENU', pantalla=pantalla, on_click=self.click_return_menu, on_click_param='form_main_menu')


        self.widget_list = [
            self.enter_name_title, self.enter_name_subtitle, self.confirmation_button, self.button_return_menu
        ]

    def click_confirm_name(self, param: str):
        self.confirm_name = True
        nombre = self.text_box.writing.strip()           # Obtenemos el nombre del TextBox
        if nombre:
            logic = Logic()
            logic.acatualizar_ranking(nombre, self.score)
            print(f'{nombre} - Score: {self.score}')
        self.set_active('form_main_menu')

    def click_return_menu(self, param):
        self.set_active(param)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        self.text_box.draw()
        self.writing_text = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-40, texto=f'{self.text_box.writing.upper()}', pantalla=self.pantalla)
        self.writing_text.draw()

    def update(self, event_list):
        super().draw()
        self.text_box.update(event_list)
        for widget in self.widget_list:
            widget.update()