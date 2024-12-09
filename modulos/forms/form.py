from ..widgets.sonido import Sonido

class Form:

    forms_dict = {}

    def __init__(self, name: str, pantalla, x: int, y: int, active: bool, level_num: int, music_path: str):
        self.forms_dict[name] = self
        self.pantalla = pantalla
        self.active = active
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_path = music_path
        self.admin_snd = Sonido()

    def set_active(self, name: str):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

        if name == 'form_ranking':
            self.forms_dict[name].cargar_ranking()
        
        if name in ['form_game', 'form_enter_name', 'form_main_menu']:
            self.forms_dict[name].music_update()
        
        if name == 'form_game':
            self.forms_dict[name].reiniciar_puntaje()


    def music_update(self):
        self.admin_snd.detener_musica()
        self.admin_snd.reproducir_musica(f'{self.music_path}')
        

    def draw(self):
        self.pantalla.blit(self.surface, self.slave_rect)
