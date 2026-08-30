# main.py (Pseudocódigo ilustrativo)
import numpy as np
import cv2 as cv
import sys
from modulos.camara import Camara
from modulos.detector import DetectorManos
from modulos.gestos import Gestos
from modulos.sistema import ControladorMouse

def main():
    mi_camara = Camara()
    mi_detector = DetectorManos()   
    mi_gesto = Gestos(15)
    mi_mouse = ControladorMouse()
        
    try:
        while True:
            frame = mi_camara.leer_frame()
            if frame is None:
                break
            frame_espejo = cv.flip(frame, 1)
            
            frame, lista_puntos = mi_detector.encontrar_manos(frame_espejo)
            if len(lista_puntos) != 0:
                id = mi_gesto.detectar_gestos(lista_puntos)
                if id == "CLICK":
                    mi_mouse.ejecutar_click(id)
                elif id == "MOVER":
                    alto, ancho, canales = frame.shape
                    mi_mouse.mover_mouse(lista_puntos[8][1], lista_puntos[8][2], alto, ancho)
                print(f"Dedo Índice en: {lista_puntos[8]}")

            cv.imshow('JARVIS Vision', frame)

            if cv.waitKey(1) == ord('q'):
                break
    finally:
        mi_camara.liberar()
        
        
if __name__ == "__main__":
    main()

