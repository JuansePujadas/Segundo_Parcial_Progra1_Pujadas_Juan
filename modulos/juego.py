import sys, pygame
from modulos.forms import FormManager
from modulos.variables import DIMENSION_PANTALLA
from modulos.auxiliar import cargar_ranking

def iniciar_juego():
    pygame.init()

    pantalla = pygame.display.set_mode(DIMENSION_PANTALLA, pygame.SCALED)
    pygame.display.set_caption('This or That')

    juego_ejecutando = True

    ranking = cargar_ranking()

    forms = FormManager(pantalla, ranking)

    while juego_ejecutando:
        event_list = pygame.event.get()
        
        for event in event_list:
            if event.type == pygame.QUIT:
                juego_ejecutando = False

        forms.update(event_list)
        pygame.display.update()
        
    pygame.quit()
    sys.exit()