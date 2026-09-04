import math
from config.loader import config_app

class Gestos:
    umbrales = config_app.obtener_interaccion()

    def __init__(self, umbral):
        self.umbral_click = umbral
        self.click_izq_apretado = False
        self.click_der_apretado = False
        self.margen_soltar = 15 
    
    def distancia_click(self, dedo1, dedo2):
        dx = dedo1[1] - dedo2[1]
        dy = dedo1[2] - dedo2[2]
        return math.hypot(dx, dy)
    
    def detectar_click(self, distancia, tipo="left"):
        """Evalúa la distancia y devuelve True si el click debe estar apretado, False si no."""
        if tipo == "left":
            if not self.click_izq_apretado and distancia < self.umbral_click:
                self.click_izq_apretado = True
            elif self.click_izq_apretado and distancia > (self.umbral_click + self.margen_soltar):
                self.click_izq_apretado = False
            return self.click_izq_apretado
            
        elif tipo == "right":
            if not self.click_der_apretado and distancia < self.umbral_click:
                self.click_der_apretado = True
            elif self.click_der_apretado and distancia > (self.umbral_click + self.margen_soltar):
                self.click_der_apretado = False
            return self.click_der_apretado
            
        return False
        
    def detectar_gestos(self, lista_puntos):
        if not lista_puntos:
            return "NADA"
        
        y_indice = lista_puntos[8][2] < lista_puntos[6][2]
        y_medio = lista_puntos[12][2] < lista_puntos[10][2]
        if y_medio and y_indice:
            return "SCROLL"
        return "MOVER"
