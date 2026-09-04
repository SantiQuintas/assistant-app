import collections
import math
import time

class MovementAnalyzer():

    def __init__(self, leng):
        self.historial = collections.deque(maxlen=leng)
        self.historial2 = collections.deque(maxlen=leng*2)
    
    def agregar_dato(self, dato):
        self.historial.append((dato, time.time()))
        self.historial2.append((dato, time.time()))
    def analizar(self, leng):
        if leng is None or leng ==0:
            leng = 5
            
        if len(self.historial) < leng:
            return {"direccion": None,
                    "confianza" : None, 
                    "desplazamiento" : None,
                    "velocidad" : None}
        else:
            direccion = "ESTATICO"
            confianza = None
            nivel_confianza = 0
            desplazamiento = 0
            absoluto = 0
            velocidad = 0
            for i in range(leng-1):
                if self.historial[i][0] < self.historial[i+1][0]:
                    nivel_confianza+=1
                elif self.historial[i][0] > self.historial[i+1][0]:
                    nivel_confianza-=1
                absoluto += abs(self.historial[i][0] - self.historial[i+1][0])
            
            tiempo_total = self.historial[-1][1] - self.historial[0][1]
            desplazamiento = self.historial[-1][0] - self.historial[0][0]
            
            velocidad = desplazamiento / tiempo_total if tiempo_total > 0 else 0
            
            abs_conf = abs(nivel_confianza)
            if abs_conf >= 2:
                if desplazamiento < -2:
                    direccion = "-"
                elif desplazamiento > 2:
                    direccion = "+"
                    
            if absoluto < 12 and direccion == "ESTATICO":
                return {"direccion": direccion,
                        "confianza" : "MUY ALTA", 
                        "desplazamiento" : desplazamiento,
                        "velocidad" : velocidad}
            if absoluto < 16 and direccion == "ESTATICO":
                return {"direccion": direccion,
                                    "confianza" : "ALTA", 
                                    "desplazamiento" : desplazamiento  ,
                                    "velocidad" : velocidad}
                
            if absoluto < 20 and direccion == "ESTATICO":
                 return {"direccion": direccion,
                                        "confianza" : "MEDIA", 
                                        "desplazamiento" : desplazamiento,
                                        "velocidad" : velocidad}
            if abs_conf == leng-1:
                confianza = "MUY ALTA"
                
            elif abs_conf >= math.trunc(leng/1.6) and  abs_conf < leng-1:
                confianza = "ALTA"
                
            elif abs_conf >= math.trunc(leng/2.5) and  abs_conf < math.trunc(leng/1.6):
                confianza = "MEDIA"
                
            elif abs_conf >= math.trunc(leng/leng) and abs_conf < math.trunc(leng/2.5):
                confianza = "BAJA"
            else:
                confianza = "INCIERTA"
            
            
            return {"direccion": direccion,
                    "confianza" : confianza,
                    "desplazamiento" : desplazamiento,
                    "velocidad" : velocidad}
            
    def analizar2(self):
                leng = 10
                    
                if len(self.historial2) < leng:
                    return {"direccion": None,
                                "confianza" : None, 
                                "desplazamiento" : None,
                                "velocidad" : None}
                else:
                    direccion = "ESTATICO"
                    confianza = None
                    nivel_confianza = 0
                    desplazamiento = 0
                    absoluto = 0
                    velocidad = 0
                    for i in range(leng-1):
                        if self.historial2[i][0] < self.historial2[i+1][0]:
                            nivel_confianza+=1
                        elif self.historial2[i][0] > self.historial2[i+1][0]:
                            nivel_confianza-=1
                        absoluto += abs(self.historial2[i][0] - self.historial2[i+1][0])
                    
                    tiempo_total = self.historial2[-1][1] - self.historial2[0][1]
                    desplazamiento = self.historial2[-1][0] - self.historial2[0][0]
                    velocidad = desplazamiento / tiempo_total if tiempo_total > 0 else 0
                    abs_conf = abs(nivel_confianza)
                    if abs_conf >= 2:
                        if desplazamiento < -2:
                            direccion = "-"
                        elif desplazamiento > 2:
                            direccion = "+"
                    if absoluto < 3:
                        return {"direccion": direccion,
                                "confianza" : "MUY ALTA", 
                                "desplazamiento" : desplazamiento,
                                "velocidad" : velocidad}
                    if absoluto < 5:
                        return {"direccion": direccion,
                                            "confianza" : "ALTA", 
                                            "desplazamiento" : desplazamiento,
                                            "velocidad" : velocidad}
                        
                    if absoluto < 6:
                         return {"direccion": direccion,
                                                "confianza" : "MEDIA", 
                                                "desplazamiento" : desplazamiento,
                                                "velocidad" : velocidad}
                    if abs_conf == leng-1:
                        confianza = "MUY ALTA"
                        
                    elif abs_conf >= math.trunc(leng/1.6) and  abs_conf < leng-1:
                        confianza = "ALTA"
                        
                    elif abs_conf >= math.trunc(leng/2.5) and  abs_conf < math.trunc(leng/1.6):
                        confianza = "MEDIA"
                        
                    elif abs_conf >= math.trunc(leng/leng) and abs_conf < math.trunc(leng/2.5):
                        confianza = "BAJA"
                    else:
                        confianza = "INCIERTA"
                    
                    
                    return {"direccion": direccion,
                            "confianza" : confianza,
                            "desplazamiento" : desplazamiento,
                            "velocidad" : velocidad}