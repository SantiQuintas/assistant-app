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
        self.suavizado = 3
    
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
        
     
    def mover_mousey(self, y_cam, alto_cam, margen, velocidad):
        y_pantalla = np.interp(y_cam, (margen, alto_cam-(margen+50)), (0, self.alto_pantalla))
        if velocidad <  40:
            factor = 0.1
        elif velocidad >  300:
            factor = 1
        else: 
            factor = 0.4
        
        y_final = self.y_prev + (y_pantalla - self.y_prev) * factor
        pyautogui.moveTo(None, y_final)
        self.y_prev = y_final
        
        return self.y_prev
    
    def mover_mousex(self, x_cam, ancho_cam, margen, velocidad):
        x_pantalla = np.interp(x_cam, (margen, ancho_cam-margen), (0, self.ancho_pantalla))
        factor = 1
        if velocidad <  40:
            factor = 0.1
        elif velocidad >  300:
            factor = 1
        else: 
            factor = 0.4
            
            
        x_final = self.x_prev + (x_pantalla - self.x_prev) * factor
        pyautogui.moveTo(x_final, None)
        self.x_prev = x_final
            
        return self.x_prev
    def mover_mouse(self, x_cam, y_cam, ancho_cam, alto_cam, margen, vel_x, vel_y):
        x_pantalla = np.interp(x_cam, (margen, ancho_cam-margen), (0, self.ancho_pantalla))
        y_pantalla = np.interp(y_cam, (margen, alto_cam-(margen+50)), (0, self.alto_pantalla))
        
        velocidad_general = max(vel_x, vel_y)
        
        if velocidad_general < 40:
            factor = 0.1
        elif velocidad_general > 300:
            factor = 1.0
        else: 
            factor = 0.4
            
        x_final = self.x_prev + (x_pantalla - self.x_prev) * factor
        y_final = self.y_prev + (y_pantalla - self.y_prev) * factor
        
        pyautogui.moveTo(x_final, y_final)
        
        self.x_prev = x_final
        self.y_prev = y_final
        
        return x_final, y_final

    def ejecutar_scroll(self, direccion):
        pyautogui.scroll(direccion*3)

        
        