import pygame

class RectRojoAzul:
    def __init__(self, x, y, pantalla, color_inicial='gris'):
        self.x = x
        self.y = y
        self.pantalla = pantalla

        self.colores = {
            'gris': (169, 169, 169),
            'rojo': (255, 0, 0),
            'azul': (0, 0, 255)
        }

        self.color_actual = self.colores.get(color_inicial, self.colores['gris'])

        self.rect = pygame.Rect(self.x, self.y, 35, 35)

    def alternar_color(self, nuevo_color: str):
        if nuevo_color in self.colores:
            self.color_actual = self.colores[nuevo_color]

    def draw(self):
        pygame.draw.rect(self.pantalla, self.color_actual, self.rect)

    def update(self):
        pass
