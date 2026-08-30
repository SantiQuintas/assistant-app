import pyautogui

class ControladorMouse:
    def __init__(self):
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0 
        self.ancho_pantalla, self.alto_pantalla = pyautogui.size()
        self.click_mantenido = False
        self.x_prev, self.y_prev = 0, 0
        self.suavizado = 2
    
    def ejecutar_click(self, gesto_detectado):
        if gesto_detectado == "CLICK" and not self.click_mantenido:
            pyautogui.click()
            self.click_mantenido = True
            print("¡Click Físico Ejecutado!")
        else:
            self.click_mantenido=False
            
    
    def mover_mouse(self, x_cam, y_cam, ancho_cam, alto_cam):
        x_pantalla = (x_cam/ancho_cam) * self.ancho_pantalla
        y_pantalla = (y_cam/alto_cam) * self.alto_pantalla
        
        x_final = self.x_prev + (x_pantalla - self.x_prev)/self.suavizado
        y_final = self.y_prev + (y_pantalla - self.y_prev)/self.suavizado
        pyautogui.moveTo(x_final, y_final)
        self.x_prev, self.y_prev = x_final, y_final
            
        
        