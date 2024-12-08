import json
import random

class Logic():
    def __init__(self):
        with open('assets/preguntas.json', 'r') as archivo:
            self.preguntas = json.load(archivo)
        
        self.puntaje = 0
        self.pregunta_actual = None
        self.votaciones_realizadas = []

    def seleccionar_pregunta(self):
        self.pregunta_actual = random.choice(list(self.preguntas.values()))  # Seleccionar una pregunta aleatoria
        
        return self.pregunta_actual
    
    def realizar_votaciones(self):
        respuestas = [self.pregunta_actual['respuesta_rojo'], self.pregunta_actual['respuesta_azul']]
        
        votos = [random.choice(respuestas) for _ in range(5)]         # Simula 5 votaciones automáticas y devuelve la mayoría
        self.votaciones_realizadas = votos                            # Almacenar las votaciones
        respuesta_correcta = max(set(votos), key=votos.count)
        return respuesta_correcta 
    
    def obtener_votaciones_half(self):
        half_votos = random.sample(self.votaciones_realizadas, 2)           # Seleccionamos 2 muestras de los 5 votos
        
        return half_votos