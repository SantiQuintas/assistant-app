class MovementAnalyzer():
    def __init__(self):
        pass
    
    def analizar(self, historial):
        direccion = "ESTATICO"
        confianza = None
        nivel_confianza = 0
        desplazamiento = 0
        for i in range(len(historial)-1):
            if historial[i] < historial[i+1]:
                nivel_confianza+=1
            elif historial[i] > historial[i+1]:
                nivel_confianza-=1
        
        desplazamiento = historial[-1] - historial[0]
        abs_conf = abs(nivel_confianza)
        if abs_conf >= 2 and abs_conf != 0:
            if desplazamiento < 0:
                direccion = "-"
            elif desplazamiento > 0:
                direccion = "+"
        
        if abs_conf == 4:
            confianza = "MUY ALTA"
            
        elif abs_conf >= 3 and  abs_conf < 4:
            confianza = "ALTA"
            
        elif abs_conf >= 2 and  abs_conf < 3:
            confianza = "MEDIA"
            
        elif abs_conf >= 1 and abs_conf < 2:
            confianza = "BAJA"
        else:
            confianza = "INCIERTA"
        
        
        return {"direccion": direccion,
                "confianza" : confianza,
                "desplazamiento" : desplazamiento}

analyzer = MovementAnalyzer()
casos_de_prueba = [
        {"nombre": "Ruido en el lugar", "datos": [500, 499, 502, 501, 500]},
        {"nombre": "Movimiento claro abajo", "datos": [500, 490, 480, 470, 460]},
        {"nombre": "Movimiento claro arriba", "datos": [500, 510, 505, 515, 520]},
        {"nombre": "Movimiento rápido abajo", "datos": [500, 450, 400, 350, 300]},
        {"nombre": "Temblor leve", "datos": [500, 501, 499, 500, 498]}
    ]

for caso in casos_de_prueba:
    resultado = analyzer.analizar(caso["datos"])
    print(f"Prueba: {caso['nombre']}")
    print(f"Datos : {caso['datos']}")
    print(f"Output: {resultado}\n{'-'*40}")