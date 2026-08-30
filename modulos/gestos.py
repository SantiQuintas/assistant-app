import math

class Gestos:
    umbral_click = None
    def __init__(self, umbral):
        self.umbral_click = umbral
    
    def detectar_gestos(self, lista_puntos):
        if not lista_puntos:
            return "NADA"
        
        
        dx = lista_puntos[8][1] - lista_puntos[4][1]
        dy = lista_puntos[8][2] - lista_puntos[4][2]
        distancia = math.hypot(dx,dy)
        
        if distancia < self.umbral_click:
            return "CLICK"
        
        y_indice = lista_puntos[8][2] < lista_puntos[6][2]
        y_medio = lista_puntos[12][2] < lista_puntos[10][2]
        if y_medio and y_indice:
            return "SCROLL"
        return "MOVER"
            
        