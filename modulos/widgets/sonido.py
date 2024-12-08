import pygame.mixer as mixer

class Sonido():
    def __init__(self):
        mixer.init()

    def reproducir_sonido(self, ruta_sonido: str):
        sonido = mixer.Sound(ruta_sonido)
        sonido.set_volume(0.7)
        sonido.play()

    def reproducir_musica(self, ruta_musica: str):
        mixer.music.load(ruta_musica)
        mixer.music.set_volume(0.3)
        mixer.music.play(-1, 0, 1000)

    def detener_musica(self):
        mixer.music.fadeout(500)        