#!/usr/bin/env python3
import cv2 as cv
import sys
from modulos.camara import Camara
from modulos.detector import DetectorManos
from modulos.gestos import Gestos
from modulos.sistema import ControladorMouse
from modulos.overlay import Overlay


def menu():
    print("¿Que modo desea usar?")
    print("Para finalizar el programa presione Q")
    eleccion = input("Escriba H (holografico) o C (Clasico): \n").lower()
    
    return eleccion
    

def main():
    modo = menu()
    mi_camara = Camara()
    mi_gesto = Gestos(25)
    mi_mouse = ControladorMouse()
    visual = Overlay()
    mi_detector = DetectorManos()
    
    if modo == "c":
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

                    if id in ["right","left", "MOVER"]:
                        mi_mouse.procesar_clicks(id)
                        x,y = mi_mouse.mover_mouse(lista_puntos[8][1], lista_puntos[8][2], alto, ancho,margen)
                        visual.actualizar(x, y, id)
                    elif id == "SCROLL":
                        if y_prev_scroll == 0:
                            y_prev_scroll=lista_puntos[8][2]
                        else:
                            direccion = y_prev_scroll-lista_puntos[8][2]
                            if abs(direccion) > 5:
                                mi_mouse.procesar_clicks(id)
                                mi_mouse.ejecutar_scroll(direccion) 
                                visual.actualizar(x, y, id)
                    print(f"Dedo Índice en: {lista_puntos[8]}")

                cv.imshow('JARVIS Vision', frame)
                
                if cv.waitKey(1) == ord('q'):
                    break
        finally:
            mi_camara.liberar()
    elif modo == "h":
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
                    id = mi_gesto.detectar_gestos_int(lista_puntos)         
                    if id == "NADA":
                        mi_mouse.procesar_clicks(id)
                    if id in ["right", "MOVER", "left"]:
                        mi_mouse.procesar_clicks(id)
                        x,y = mi_mouse.mover_mouse(lista_puntos[8][1], lista_puntos[8][2], alto, ancho,margen)
                        visual.actualizar(x, y, id)
                    elif id == "SCROLL":  
                        if y_prev_scroll == 0:
                            y_prev_scroll=lista_puntos[8][2]
                        else:
                            direccion = y_prev_scroll-lista_puntos[8][2]
                            if abs(direccion) > 5:
                                mi_mouse.procesar_clicks(id)
                                mi_mouse.ejecutar_scroll(direccion) 
                                visual.actualizar(x, y, id)
                cv.imshow('JARVIS Vision', frame)
                            
                if cv.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:
            mi_camara.liberar()
    else:
        print("Opcion No Valida")
        sys.exit(1)
        

