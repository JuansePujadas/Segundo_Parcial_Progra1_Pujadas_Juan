import pygame
from .variables import RANKING_FILE

def generar_imagen(ruta_imagen: str, divisor_achique: int = 1) -> pygame.Surface:
    imagen = pygame.image.load(ruta_imagen)
    alto = imagen.get_height() // divisor_achique
    ancho = imagen.get_width() // divisor_achique
    imagen_final = pygame.transform.scale(imagen, (ancho, alto))
    return imagen_final

def ordenar_matriz(matriz):
    for i in range(len(matriz) - 1):
        for j in range(i+1, len(matriz)):
            if int(matriz[i][1]) < int(matriz[j][1]):
                matriz[i], matriz[j] =\
                matriz[j], matriz[i]

def cargar_ranking():
    ranking = []

    with open(RANKING_FILE, 'r') as ranking_file:
        lineas = ranking_file.read()
        for linea in lineas.split('\n'):
            fila = linea.split(',')
            if len(fila) == 2 and fila[0].strip() and fila[1].strip():        # Aseguramos que haya dos elementos y no sean vacíos
                ranking.append(fila)

    ranking = [fila for fila in ranking if fila]                              # Aseguramos que no haya filas vacías al final de la lista

    ordenar_matriz(ranking)
    
    return ranking