import cv2 as cv
import sys

class Camara:
    camara = None
    
    def __init__(self):
        self.camara = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.camara.isOpened():
            print("No se puede abrir la camara")
            self.camara = cv.VideoCapture(1, cv.CAP_DSHOW)
            if not self.camara.isOpened():
                print("Error crítico: No se encuentra ninguna cámara.")
                sys.exit(1)   
                 
    def leer_frame(self):
        ret, frame= self.camara.read()
        if not ret:
            print("No se recibio fotograma (termino la captura de video?)")
            return None
        else:
            return frame            
            
    def liberar(self):
            self.camara.release()
            cv.destroyAllWindows()