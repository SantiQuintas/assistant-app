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
    mi_gesto = Gestos(25)
    mi_mouse = ControladorMouse()
    visual = Overlay()
    mi_detector = DetectorManos()
    analyzer_indicex = MovementAnalyzer(5)
    analyzer_indicey = MovementAnalyzer(5)
    analyzer_distancia_click = MovementAnalyzer(5)
    analyzer_distancia_clickd = MovementAnalyzer(5)
    hubo_click = False
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
                if modo == "h":
                    id = mi_gesto.detectar_gestos_int(lista_puntos)
                elif(modo == "c"):
                    id = mi_gesto.detectar_gestos(lista_puntos)
                else:
                    break
                
                analyzer_indicex.agregar_dato(lista_puntos[8][1])
                analyzer_indicey.agregar_dato(lista_puntos[8][2])
                analyzer_distancia_click.agregar_dato(mi_gesto.distancia_click(lista_puntos[12], lista_puntos[4]))
                analyzer_distancia_clickd.agregar_dato(mi_gesto.distancia_click(lista_puntos[20], lista_puntos[4]))
                cc = analyzer_distancia_click.analizar(5)
                ccd = analyzer_distancia_clickd.analizar(5)
                cx = analyzer_indicex.analizar(5)
                cy = analyzer_indicey.analizar(5)
                if cc['confianza'] is not None and ccd['confianza'] is not None and cx['confianza'] is not None and cy['confianza'] is not None: 
                    if id not in ["right", "left"]:
                        if hubo_click == True and cc['confianza'] in ["MUY ALTA", "ALTA"] and cc["direccion"] == "+":
                            mi_mouse.procesar_clicks(id)
                            hubo_click = False
                        else:
                            cc = analyzer_distancia_click.analizar2()
                            if cc['confianza'] in ["MUY ALTA", "ALTA"] and cc["direccion"] == "+":
                                    mi_mouse.procesar_clicks(id)
                                    hubo_click = False
                        
                        
                
                    if id in ["right", "MOVER", "left", "SCROLL"]:


                        # ANALIZAR CLICKS (R / L)
                        if cc is not None:
                            if id =="left":
                                if cc['confianza'] in ["MUY ALTA", "ALTA"] and cc["direccion"] == "+":
                                    mi_mouse.procesar_clicks(id)
                                    hubo_click = True
                                elif cc['confianza'] in ["MEDIA", "BAJA"]:
                                    cc = analyzer_distancia_click.analizar2()
                                    if cc['confianza'] in ["MUY ALTA", "ALTA"] and cc["direccion"] == "+":
                                        mi_mouse.procesar_clicks(id)
                                        hubo_click = True
                            elif id == "right":
                                if ccd['confianza'] in ["MUY ALTA", "ALTA"] and ccd["direccion"] == "-":
                                    mi_mouse.procesar_clicks(id)
                                elif ccd['confianza'] in ["MEDIA", "BAJA"]:
                                    ccd = analyzer_distancia_clickd.analizar2()
                                    if ccd['confianza'] in ["MUY ALTA", "ALTA"] and ccd["direccion"] == "-":
                                        mi_mouse.procesar_clicks(id)
                        
                            
                        #ANALIZAR MOVIMIENTO INDICE
                        if cx is not None and cy is not None:
                            print(f"Velocidad x : {cx['velocidad']}")
                            if cx['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"] and cy['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"]:
                                if cx['direccion'] != "ESTATICO":
                                    x= mi_mouse.mover_mousex(lista_puntos[8][1], ancho, margen, cx['velocidad'])
                                    
                                    
                                if cy['direccion'] != "ESTATICO":
                                    y= mi_mouse.mover_mousey(lista_puntos[8][2], alto, margen, cy['velocidad'])
                                    
                            elif cx['confianza'] in ["BAJA", "INCIERTA"] and cy['confianza'] not in ["MUY BAJA", "INCIERTA"]:
                                cx = analyzer_indicex.analizar2()
                                cy = analyzer_indicey.analizar2()
                                if cx['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"] and cy['confianza'] in ["MUY ALTA", "ALTA", "MEDIA"]:
                                    if cx['direccion'] != "ESTATICO":
                                        x= mi_mouse.mover_mousex(lista_puntos[8][1], ancho, margen, cx['velocidad'])
                                        
                                    if cy['direccion'] != "ESTATICO":
                                        y= mi_mouse.mover_mousey(lista_puntos[8][2], alto, margen, cy['velocidad'])    
                                
                    elif id == "SCROLL":  
                        if y_prev_scroll == 0:
                            y_prev_scroll=lista_puntos[8][2]
                        else:
                            direccion = y_prev_scroll-lista_puntos[8][2]
                            if abs(direccion) > 5:
                                mi_mouse.ejecutar_scroll(direccion)
                      
                    
            cv.imshow('JARVIS Vision', frame)
                            
            if cv.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
            mi_camara.liberar()

        
if __name__ == "__main__":
    main()