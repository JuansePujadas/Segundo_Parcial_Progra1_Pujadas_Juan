import pygame
from .form import Form
from ..widgets import (TextTitle, Button)
from ..variables import (DIMENSION_PANTALLA, RUTA_FONDO_PARTIDA)
#from ..logica import Logic

class FormGame(Form):
    def __init__(self, name, pantalla, x, y, active, level_num, music_path, logic):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        self.logic = logic
        self.music_update()

        self.surface = pygame.image.load(RUTA_FONDO_PARTIDA).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.score = 0
        self.game_over = False

        self.game_title_pregunta = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-200, texto='PREGUNTA', pantalla=pantalla, font_size=22)
        self.game_title_puntaje = TextTitle(x=DIMENSION_PANTALLA[0]//2-350, y=DIMENSION_PANTALLA[1]//2+275, texto=f'{self.score}', pantalla=pantalla, font_size=35)
        self.game_boton_rojo = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-50, texto='RESP 1', pantalla=pantalla, on_click=self.responder_rojo, on_click_param='rojo')
        self.game_boton_azul = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-100, texto='RESP 2', pantalla=pantalla, on_click=self.responder_azul, on_click_param='azul')

        self.widget_list = [self.game_title_pregunta, self.game_title_puntaje, self.game_boton_rojo, self.game_boton_azul]

        self.actualizar_pregunta()

    def actualizar_puntaje(self, respuesta_correcta):
        if respuesta_correcta:
            self.score += 10
        self.game_title_puntaje.texto = f'{self.score}'

    def responder_rojo(self, opcion):
        if self.logic.pregunta_actual:
            respuesta_correcta = (opcion == 'rojo' and self.logic.pregunta_actual['respuesta_rojo'] == self.logic.realizar_votaciones())
            self.actualizar_puntaje(respuesta_correcta)
            self.actualizar_pregunta()

    def responder_azul(self, opcion):
        if self.logic.pregunta_actual:
            respuesta_correcta = (opcion == 'azul' and self.logic.pregunta_actual['respuesta_azul'] == self.logic.realizar_votaciones())
            self.actualizar_puntaje(respuesta_correcta)
            self.actualizar_pregunta()

    def actualizar_pregunta(self):
        self.logic.seleccionar_pregunta()
        self.game_title_pregunta.texto = self.logic.pregunta_actual['pregunta']
        self.game_boton_rojo.texto = self.logic.pregunta_actual['respuesta_rojo']
        self.game_boton_azul.texto = self.logic.pregunta_actual['respuesta_azul']

        for widget in self.widget_list:
            widget.update()

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()

    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()