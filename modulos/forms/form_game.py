import pygame
from .form import Form
from ..widgets import (TextTitle, Button, RectRojoAzul)
from ..variables import (DIMENSION_PANTALLA, RUTA_FONDO_PARTIDA, COLOR_AZUL, COLOR_ROJO)
from ..logica import *

class FormGame(Form):
    def __init__(self, name, pantalla, x, y, active, level_num, music_path, logic):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        self.logic = logic

        self.surface = pygame.image.load(RUTA_FONDO_PARTIDA).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.score = 0
        #self.game_over = False

        self.game_title_pregunta = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-200, texto='PREGUNTA', pantalla=pantalla, font_size=22)
        self.game_title_puntaje = TextTitle(x=DIMENSION_PANTALLA[0]//2-350, y=DIMENSION_PANTALLA[1]//2+275, texto=f'{self.score}', pantalla=pantalla, font_size=35)
        self.game_boton_rojo = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-50, texto='RESP 1', pantalla=pantalla, font_size=35, on_click=self.responder_rojo, on_click_param='rojo', color=COLOR_ROJO)
        self.game_boton_azul = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-100, texto='RESP 2', pantalla=pantalla, font_size=35, on_click=self.responder_azul, on_click_param='azul', color=COLOR_AZUL)
        self.game_rect_votante1 = RectRojoAzul(x=DIMENSION_PANTALLA[0]//2-8, y=DIMENSION_PANTALLA[1]//2+75, pantalla=pantalla)
        self.game_rect_votante2 = RectRojoAzul(x=DIMENSION_PANTALLA[0]//2+110, y=DIMENSION_PANTALLA[1]//2+75, pantalla=pantalla)
        self.game_rect_votante3 = RectRojoAzul(x=DIMENSION_PANTALLA[0]//2+225, y=DIMENSION_PANTALLA[1]//2+75, pantalla=pantalla)
        self.game_rect_votante4 = RectRojoAzul(x=DIMENSION_PANTALLA[0]//2-125, y=DIMENSION_PANTALLA[1]//2+75, pantalla=pantalla)
        self.game_rect_votante5 = RectRojoAzul(x=DIMENSION_PANTALLA[0]//2-228, y=DIMENSION_PANTALLA[1]//2+75, pantalla=pantalla)


        self.widget_list = [self.game_title_pregunta, self.game_title_puntaje, self.game_boton_rojo, self.game_boton_azul, self.game_rect_votante1, self.game_rect_votante2, self.game_rect_votante3, self.game_rect_votante4, self.game_rect_votante5]

        self.mostrar_colores_tiempo = None
        self.pregunta_actualizada = False
        self.actualizar_pregunta()

    def reiniciar_puntaje(self):  # Método para reiniciar el puntaje al comienzo de la partida
        self.score = 0
        self.game_title_puntaje.texto = f'{self.score}'

    def actualizar_puntaje(self, respuesta_correcta):
        if respuesta_correcta:
            self.score += 10
        self.game_title_puntaje.texto = f'{self.score}'

    def responder_rojo(self, opcion):
        if self.logic.pregunta_actual:
            respuesta_correcta = (opcion == 'rojo' and self.logic.pregunta_actual['respuesta_rojo'] == self.logic.realizar_votaciones())
            self.actualizar_puntaje(respuesta_correcta)
            self.mostrar_colores()
            
            if respuesta_correcta:
                self.pregunta_actualizada = False
            else:                
                self.logic.finalizar_partida(self.score)

    def responder_azul(self, opcion):
        if self.logic.pregunta_actual:
            respuesta_correcta = (opcion == 'azul' and self.logic.pregunta_actual['respuesta_azul'] == self.logic.realizar_votaciones())
            self.actualizar_puntaje(respuesta_correcta)
            self.mostrar_colores()
            
            if respuesta_correcta:
                self.pregunta_actualizada = False
            else:                
                self.logic.finalizar_partida(self.score)

    def mostrar_colores(self):
        votos = self.logic.votaciones_realizadas
        print(f'{votos}')

        respuesta_rojo = self.logic.pregunta_actual['respuesta_rojo']
        
        for i, rect in enumerate(self.widget_list[4:]):  # Empezamos desde el índice de los rectángulos
            if votos[i] == respuesta_rojo:
                rect.alternar_color('rojo')
            else:
                rect.alternar_color('azul')

        self.mostrar_colores_tiempo = pygame.time.get_ticks()

    def actualizar_pregunta(self):
        self.logic.seleccionar_pregunta()
        self.game_title_pregunta.texto = self.logic.pregunta_actual['pregunta']
        self.game_boton_rojo.texto = self.logic.pregunta_actual['respuesta_rojo']
        self.game_boton_azul.texto = self.logic.pregunta_actual['respuesta_azul']

        self.resetear_colores()

        for widget in self.widget_list:
            widget.update()

    def resetear_colores(self):
        for rect in self.widget_list[4:]:
            rect.alternar_color('gris')

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()

    def update(self):
        # Mostrar los colores por 3 segundos
        if self.mostrar_colores_tiempo is not None:
            if pygame.time.get_ticks() - self.mostrar_colores_tiempo < 3000:
                # Mientras han pasado menos de 3 segundos, seguir mostrando los colores
                self.draw()
                return  # No continuar con la actualización, esperar 3 segundos
            else:
                # Después de 3 segundos, actualizar la pregunta o finalizar la partida
                self.mostrar_colores_tiempo = None  # Resetear el temporizador
                if not self.pregunta_actualizada:
                    self.actualizar_pregunta()  # Ahora actualizamos la pregunta
                    self.pregunta_actualizada = True  # Evitar actualización inmediata

                for widget in self.widget_list:
                    widget.update()  # Continuar con la actualización normal de widgets

                # Ahora se puede proceder a actualizar la pregunta o finalizar la partida
                if self.logic.realizar_votaciones():
                    self.actualizar_pregunta()
                else:
                    self.logic.finalizar_partida(self.score)
        else:
            for widget in self.widget_list:
                widget.update()