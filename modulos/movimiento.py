import collections
import math

class MovementAnalyzer():

    def __init__(self, leng):
        self.historial = collections.deque(maxlen=leng)

    
    def agregar_dato(self, dato):
        self.historial.append(dato)
        
    def analizar(self, leng):
        if leng is None or leng ==0:
            leng = 5
            
        if len(self.historial) < leng:
            return None
        else:
            direccion = "ESTATICO"
            confianza = None
            nivel_confianza = 0
            desplazamiento = 0
            absoluto = 0
            for i in range(leng-1):
                if self.historial[i] < self.historial[i+1]:
                    nivel_confianza+=1
                elif self.historial[i] > self.historial[i+1]:
                    nivel_confianza-=1
                absoluto += abs(self.historial[i] - self.historial[i+1])
                    
            desplazamiento = self.historial[-1] - self.historial[0]
            abs_conf = abs(nivel_confianza)
            if abs_conf >= 2:
                if desplazamiento < 0:
                    direccion = "-"
                elif desplazamiento > 0:
                    direccion = "+"
            if absoluto < 10 and desplazamiento < 5 and desplazamiento > -5:
                return {"direccion": direccion,
                        "confianza" : "MUY ALTA", 
                        "desplazamiento" : desplazamiento}
            if absoluto < 12 and desplazamiento < 8 and desplazamiento > -8:
                return {"direccion": direccion,
                                    "confianza" : "ALTA", 
                                    "desplazamiento" : desplazamiento}
                
            if absoluto < 15 and desplazamiento < 10 and desplazamiento > -10:
                 return {"direccion": direccion,
                                        "confianza" : "MEDIA", 
                                        "desplazamiento" : desplazamiento}
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
                    "desplazamiento" : desplazamiento}
