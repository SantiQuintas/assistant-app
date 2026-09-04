#!/usr/bin/env python3
import cv2 as cv
import sys
from modulos.camara import Camara
from modulos.detector import DetectorManos
from modulos.gestos import Gestos
from modulos.sistema import ControladorMouse
from modulos.overlay import Overlay
from modulos.movimiento import MovementAnalyzer

def menu():
    print("¿Que modo desea usar?")
    print("Para finalizar el programa presione Q")
    eleccion = input("Escriba H (holografico) o C (Clasico): \n").lower()
    return eleccion
    
def main():
    modo = menu()
    mi_camara = Camara()
    # Le subí un pelín el umbral a 20 para que sea más cómodo
    mi_gesto = Gestos(20) 
    mi_mouse = ControladorMouse()
    visual = Overlay()
    mi_detector = DetectorManos()
    
    # Solo necesitamos MovementAnalyzer para las coordenadas X e Y (estabilidad)
    analyzer_indicex = MovementAnalyzer(5)
    analyzer_indicey = MovementAnalyzer(5)
    
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
                distancia_izq = mi_gesto.distancia_click(lista_puntos[12], lista_puntos[4])
                distancia_der = mi_gesto.distancia_click(lista_puntos[20], lista_puntos[4])
                
                hubo_click_izq = mi_gesto.detectar_click(distancia_izq, "left")
                hubo_click_der = mi_gesto.detectar_click(distancia_der, "right")
                
                mi_mouse.procesar_clicks(hubo_click_izq, hubo_click_der)

                id_gesto = mi_gesto.detectar_gestos(lista_puntos)
                
                analyzer_indicex.agregar_dato(lista_puntos[8][1])
                analyzer_indicey.agregar_dato(lista_puntos[8][2])
                cx = analyzer_indicex.analizar(5)
                cy = analyzer_indicey.analizar(5)
                
    
                if cx is not None and cy is not None:
                    if cx['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"] and cy['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"]:

                        if cx['direccion'] != "ESTATICO":

                            if cy['direccion'] != "ESTATICO":

                                x, y= mi_mouse.mover_mouse(lista_puntos[8][1], lista_puntos[8][2], ancho, alto, margen)

                            else:

                                x= mi_mouse.mover_mousex(lista_puntos[8][1], ancho, margen)

                        elif cy['direccion'] != "ESTATICO":

                            y= mi_mouse.mover_mousey(lista_puntos[8][2], alto, margen)
                                            
                    elif cx['confianza'] in ["BAJA", "INCIERTA"] and cy['confianza'] not in ["MUY BAJA", "INCIERTA"]:
                        cx = analyzer_indicex.analizar2()
                        cy = analyzer_indicey.analizar2()

                        if cx['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"] and cy['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"]:
                            if cx['direccion'] != "ESTATICO":

                                if cy['direccion'] != "ESTATICO":
                                    x, y= mi_mouse.mover_mouse(lista_puntos[8][1], lista_puntos[8][2], ancho, alto, margen)
                                else:
                                    x= mi_mouse.mover_mousex(lista_puntos[8][1], ancho, margen)

                            elif cy['direccion'] != "ESTATICO":
                                y= mi_mouse.mover_mousey(lista_puntos[8][2], alto, margen)
                
          
                if id_gesto == "SCROLL":  
                    if y_prev_scroll == 0:
                        y_prev_scroll = lista_puntos[8][2]
                    else:
                        direccion_scroll = y_prev_scroll - lista_puntos[8][2]
                        if abs(direccion_scroll) > 5:
                            mi_mouse.ejecutar_scroll(direccion_scroll)
                else:
                    y_prev_scroll = 0 
                    
            cv.imshow('JARVIS Vision', frame)
                            
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        mi_camara.liberar()

if __name__ == "__main__":
    main()