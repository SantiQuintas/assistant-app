# main.py (Pseudocódigo ilustrativo)
import numpy as np
import cv2 as cv
import sys
from modulos.camara import Camara
from modulos.detector import DetectorManos
from modulos.gestos import Gestos
from modulos.sistema import ControladorMouse
from modulos.overlay import CursorVisual

def main():
    mi_camara = Camara()
    mi_detector = DetectorManos()   
    mi_gesto = Gestos(25)
    mi_mouse = ControladorMouse()
    mi_cursor = CursorVisual()
        
    try:
        y_prev_scroll = 0
        while True:
            frame = mi_camara.leer_frame()
            if frame is None:
                break
            frame_espejo = cv.flip(frame, 1)
            
            frame, lista_puntos = mi_detector.encontrar_manos(frame_espejo)
            alto, ancho, canales = frame.shape
            margen = 100
            cv.rectangle(frame, (margen,margen), ((ancho-margen),(alto-margen)), (255,0,255), 2 )
            
            if len(lista_puntos) != 0:
                id = mi_gesto.detectar_gestos(lista_puntos)
                click = id == "CLICK"
                if id in ["CLICK", "MOVER"]:
                    mi_mouse.procesar_clicks(click)
                    x,y = mi_mouse.mover_mouse(lista_puntos[8][1], lista_puntos[8][2], alto, ancho,margen)
                    mi_cursor.actualizar(x, y, click)
                elif id == "SCROLL":
                    
                    if y_prev_scroll == 0:
                        y_prev_scroll=lista_puntos[8][2]
                    else:
                        direccion = y_prev_scroll-lista_puntos[8][2]
                        if abs(direccion) > 5:
                            mi_mouse.procesar_clicks(False)
                            mi_mouse.ejecutar_scroll(direccion) 
                            mi_cursor.actualizar(x, y, click)
                print(f"Dedo Índice en: {lista_puntos[8]}")

            cv.imshow('JARVIS Vision', frame)
            
            if cv.waitKey(1) == ord('q'):
                break
    finally:
        mi_camara.liberar()
        
if __name__ == "__main__":
    main()

