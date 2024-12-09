import pygame
from ..variables import RUTA_MUSICA_LOBBY, RUTA_MUSICA_PARTIDA, RUTA_SONIDO_LOSER
from .form_main_menu import FormMainMenu
from .form_ranking import FormRanking
from .form_enter_name import FormEnterName
from .form_game import FormGame
from ..logica import Logic

class FormManager:
    def __init__(self, pantalla, ranking=None):
        
        self.main_screen = pantalla
        self.ranking = ranking

        self.logic = Logic()

        self.forms = [
            FormMainMenu(name='form_main_menu', pantalla=pantalla, x=0, y=0, active=True, level_num=1, music_path=RUTA_MUSICA_LOBBY), 
            FormRanking(name='form_ranking', pantalla=pantalla, x=0, y=0, active=True, level_num=1, music_path=RUTA_MUSICA_LOBBY, ranking_list=self.ranking),
            FormGame(name='form_game', pantalla=pantalla, x=0, y=0, active=True, level_num=1, music_path=RUTA_MUSICA_PARTIDA, logic=self.logic),
            FormEnterName(name='form_enter_name', pantalla=pantalla, x=0, y=0, active=True, level_num=1, music_path=RUTA_SONIDO_LOSER, score=0)
        ]
    
    def form_update(self, event_list):

        if self.forms[0].active:
            self.forms[0].update()
            self.forms[0].draw()
        
        elif self.forms[1].active:
            self.forms[1].update()
            self.forms[1].draw()

        elif self.forms[2].active:
            self.forms[2].update()
            self.forms[2].draw()

        elif self.forms[3].active:
            self.forms[3].update(event_list)
            self.forms[3].draw()

    def update(self, event_list):
        self.form_update(event_list)