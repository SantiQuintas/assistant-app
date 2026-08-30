import math

class Gestos:
    umbral_click = None
    def __init__(self, umbral):
        self.umbral_click = umbral
    
    def detectar_gestos(self, lista_puntos):
        if not lista_puntos:
            return False
        
        
        dx = lista_puntos[8][1] - lista_puntos[4][1]
        dy = lista_puntos[8][2] - lista_puntos[4][2]
        distancia = math.hypot(dx,dy)
        
        if distancia < self.umbral_click:
            return "CLICK"
        
        return "MOVER"
            
        