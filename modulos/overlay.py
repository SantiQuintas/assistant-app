import tkinter as tk

class CursorVisual:
    
    def __init__(self):
        self.root =tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.color_transparente = "black"
        self.root.attributes("-transparentcolor", self.color_transparente)
        self.radio = 25
        self.root.geometry(f"{self.radio*2}x{self.radio*2}+0+0")
        self.canvas = tk.Canvas(self.root, width=self.radio*2, height=self.radio*2, 
                                bg=self.color_transparente, highlightthickness=0)
        self.canvas.pack()
        
        # Dibujamos el círculo inicial (Verde, indicando movimiento)
        self.circulo = self.canvas.create_oval(2, 2, self.radio*2-2, self.radio*2-2, 
                                               outline="white", width=3)
        
    def actualizar(self, x_pantalla, y_pantalla, click):
       
        pos_x = int(x_pantalla - self.radio)
        pos_y = int(y_pantalla - self.radio)
        self.root.geometry(f"+{pos_x}+{pos_y}")
        
        if click:
            self.canvas.itemconfig(self.circulo, outline="red", width=5)
        else:
            self.canvas.itemconfig(self.circulo, outline="white", width=3)
            
        self.root.update()
        