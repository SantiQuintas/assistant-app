import json
import os

class Configuracion():
    def __init__(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_destino = os.path.join(ruta_actual, "config.json")
    
        with open (ruta_destino, "r") as f:
            self.datos = json.load(f)
            
    def obtener_interaccion(self):
        return self.datos.get("interaccion", {})


config_app = Configuracion()         
                