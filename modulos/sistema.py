import pyautogui
import numpy as np

class ControladorMouse:
    def __init__(self):
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0 
        self.ancho_pantalla, self.alto_pantalla = pyautogui.size()
        self.click_mantenido = False
        self.clickd_mantenido = False
        self.x_prev, self.y_prev = 0, 0
        self.suavizado = 5
    
    def procesar_clicks(self, gesto_detectado):
        if gesto_detectado in ["left", "right"] and not self.click_mantenido:
            pyautogui.mouseDown(button = gesto_detectado)
            if gesto_detectado == "left":
                self.click_mantenido = True
            else:
                self.clickd_mantenido = True
            print("¡Click Físico Ejecutado!")
        elif gesto_detectado != "left" and self.click_mantenido:
            pyautogui.mouseUp(button = "left")
            self.click_mantenido=False
        elif gesto_detectado != "right" and self.clickd_mantenido:
            pyautogui.mouseUp(button = "right")
            self.clickd_mantenido=False
        
     
    
    def mover_mouse(self, x_cam, y_cam, ancho_cam, alto_cam, margen):
        x_pantalla = np.interp(x_cam, (margen, ancho_cam-margen), (0, self.ancho_pantalla))
        x_final = self.x_prev + (x_pantalla - self.x_prev)/self.suavizado
        y_pantalla = np.interp(y_cam, (margen, alto_cam-(margen+200)), (0, self.alto_pantalla))
        y_final = self.y_prev + (y_pantalla - self.y_prev)/self.suavizado
        

        pyautogui.moveTo(x_final, y_final)
   
        self.x_prev, self.y_prev = x_final, y_final
        
        return self.x_prev, self.y_prev

    def ejecutar_scroll(self, direccion):
        pyautogui.scroll(direccion*3)

        
        