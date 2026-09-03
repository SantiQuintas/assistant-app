import math
from config.loader import config_app

class Gestos:
    umbrales = config_app.obtener_interaccion()

    def __init__(self, umbral):
        self.umbral_click = umbral
    
    
    def distancia_click(self, dedo1, dedo2):
        dx = dedo1[1] - dedo2[1]
        dy = dedo1[2] - dedo2[2]
        distancia = math.hypot(dx,dy)

        return distancia
    
    def detectar_gestos(self, lista_puntos):
        if not lista_puntos:
            return "NADA"
        
        
        distancia = self.distancia_click(lista_puntos[12], lista_puntos[4])
        distancia2 = self.distancia_click(lista_puntos[20], lista_puntos[4])
        
        if distancia < self.umbral_click:
            return "left"
        
        if distancia2 < self.umbral_click:
            return "right"
        
        y_indice = lista_puntos[8][2] < lista_puntos[6][2]
        y_medio = lista_puntos[12][2] < lista_puntos[10][2]
        if y_medio and y_indice:
            return "SCROLL"
        return "MOVER"
    
    def estimar_profundidad(self, lista_puntos):
        dx = lista_puntos[9][1] - lista_puntos[0][1]
        dy = lista_puntos[9][2] - lista_puntos[0][2]
        distancia_mano = math.hypot(dx,dy)

        return distancia_mano
    
    
    def detectar_gestos_int(self, lista_puntos):
        if not lista_puntos:
            return "NADA"
        
        z_imaginario = self.estimar_profundidad(lista_puntos)
        pared_1 = self.umbrales.get("wall_touch")
        pared_2 = self.umbrales.get("wall_hover")
        umbral_air_tap = self.umbrales.get("air_tap_threshold")
        z_indice = abs(lista_puntos[8][3])
        
        if z_imaginario < pared_2:
            return "NADA"
        elif z_imaginario >= pared_2 and z_imaginario < pared_1:
            y_indice = lista_puntos[8][2] < lista_puntos[6][2]
            y_medio = lista_puntos[12][2] < lista_puntos[10][2]
            if y_indice and y_medio:
                return "SCROLL"
            
            return "MOVER"
        elif z_imaginario >= pared_1:
            umbral_air_tap=0.1478
            x = lista_puntos[8][1] - lista_puntos[16][1]
            y = lista_puntos[8][2] - lista_puntos[16][2]
            distancia = math.hypot(x,y)
            if distancia < 50 and z_indice > umbral_air_tap:
                return "right"
            elif z_indice > umbral_air_tap:
                return "left"
            else:
                return "MOVER"
            
            
            
        