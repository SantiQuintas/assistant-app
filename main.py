# main.py (Pseudocódigo ilustrativo)
import numpy as np
import cv2 as cv
import sys
from modulos.camara import Camara
from modulos.detector import DetectorManos


def main():
    mi_camara = Camara()
    mi_detector = DetectorManos()   

        
    try:
        while True:
            frame = mi_camara.leer_frame()
            if frame is None:
                break
            frame, lista_puntos = mi_detector.encontrar_manos(frame)
            if len(lista_puntos) != 0:
                # El índice (dedo índice) es el punto número 8. 
                # lista_puntos[8] te debería devolver: [8, coord_X, coord_Y]
                print(f"Dedo Índice en: {lista_puntos[8]}")
            cv.imshow('JARVIS Vision', frame)

            if cv.waitKey(1) == ord('q'):
                break
    finally:
        mi_camara.liberar()
        
        
if __name__ == "__main__":
    main()

