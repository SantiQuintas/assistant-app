import pyautogui
import numpy as np
from modulos.filtro import OneEuroFilter

class ControladorMouse:
    def __init__(self):
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0 
        self.ancho_pantalla, self.alto_pantalla = pyautogui.size()
        self.click_mantenido = False
        self.clickd_mantenido = False
        self.x_prev, self.y_prev = 0, 0
        self.filtro_x = OneEuroFilter(min_cutoff=0.2, beta=0.05)
        self.filtro_y = OneEuroFilter(min_cutoff=0.2, beta=0.05)
    
    def procesar_clicks(self, click_izq_activo, click_der_activo):
        # LÓGICA CLICK IZQUIERDO
        if click_izq_activo and not self.click_mantenido:
            pyautogui.mouseDown(button="left")
            self.click_mantenido = True
            print("¡Click Izquierdo Abajo!")
        elif not click_izq_activo and self.click_mantenido:
            pyautogui.mouseUp(button="left")
            self.click_mantenido = False
            print("¡Click Izquierdo Arriba!")

        # LÓGICA CLICK DERECHO
        if click_der_activo and not self.clickd_mantenido:
            pyautogui.mouseDown(button="right")
            self.clickd_mantenido = True
            print("¡Click Derecho Abajo!")
        elif not click_der_activo and self.clickd_mantenido:
            pyautogui.mouseUp(button="right")
            self.clickd_mantenido = False
            print("¡Click Derecho Arriba!")
    def mover_mousex(self, x_cam,  ancho_cam,  margen):
        x_pantalla = np.interp(x_cam, (margen, ancho_cam-margen), (0, self.ancho_pantalla))
        x_final = self.filtro_x.calcular(x_pantalla)
        pyautogui.moveTo(x_final, self.y_prev)
        self.x_prev = x_final
        return x_final
    def mover_mousey(self, y_cam,  alto_cam, margen):
        y_pantalla = np.interp(y_cam, (margen, alto_cam-(margen+100)), (0, self.alto_pantalla))
        y_final = self.filtro_y.calcular(y_pantalla)
        pyautogui.moveTo(self.x_prev, y_final)
        self.y_prev = y_final
        return y_final
        
    def mover_mouse(self, x_cam, y_cam, ancho_cam, alto_cam, margen):
        x_pantalla = np.interp(x_cam, (margen, ancho_cam-margen), (0, self.ancho_pantalla))
        y_pantalla = np.interp(y_cam, (margen, alto_cam-(margen+100)), (0, self.alto_pantalla))
        
        x_final = self.filtro_x.calcular(x_pantalla)
        y_final = self.filtro_y.calcular(y_pantalla)
        
        pyautogui.moveTo(x_final, y_final)
        
        self.x_prev = x_final
        self.y_prev = y_final
        
        return x_final, y_final

    def ejecutar_scroll(self, direccion):
        pyautogui.scroll(direccion * 3)