import json, csv
import random
from .forms.form import Form

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
        
        votos = [random.choice(respuestas) for _ in range(5)]               # Simula 5 votaciones automáticas 
        self.votaciones_realizadas = votos                                  # Almacenar las votaciones
        respuesta_correcta = max(set(votos), key=votos.count)               # Devuelve la mayoría
        return respuesta_correcta 
    
    def obtener_votaciones_half(self):
        half_votos = random.sample(self.votaciones_realizadas, 2)           # Seleccionamos 2 muestras de los 5 votos
        
        return half_votos
    
    def finalizar_partida(self, puntaje):
        if self.verificar_ingreso_ranking(puntaje):
            enter_name_form = Form.forms_dict['form_enter_name']
            enter_name_form.score = puntaje
            enter_name_form.set_active('form_enter_name')
        else:
            Form.forms_dict['form_main_menu'].set_active('form_main_menu')

    def verificar_ingreso_ranking(self, puntaje):
        with open('assets/ranking.csv', 'r') as archivo:
            lector_csv = csv.reader(archivo)
            puntajes = [int(fila[1]) for fila in lector_csv]
        
        if puntaje > min(puntajes):
            return True
        return False
    
    def acatualizar_ranking(self, nombre, puntaje):
        ranking = []

        with open('assets/ranking.csv', mode='r') as archivo:
            lector_csv = csv.reader(archivo)
            ranking = [(fila[0], int(fila[1])) for fila in lector_csv if fila and len(fila) > 1] #Filtra las filas vacías devolviendo True si tiene elementos y False si no los tiene
        
        ranking.append((nombre, puntaje))
        ranking.sort(key=lambda x: x[1], reverse=True)   #Ordena la lista ranking en orden descendente según el segundo elemento de cada tupla.
        ranking = ranking[:4]                            #Mantenemos solo al top 4 en la lista

        with open('assets/ranking.csv', mode='w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerows(ranking)