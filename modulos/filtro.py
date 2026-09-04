import math
import time

class OneEuroFilter:
    def __init__(self, min_cutoff=1.0, beta=0.01, d_cutoff=1.0):
        self.min_cutoff = min_cutoff
        self.beta = beta
        self.d_cutoff = d_cutoff
        self.x_prev = None
        self.dx_prev = 0.0
        self.t_prev = None

    def calcular(self, x):
        t = time.time()
        if self.x_prev is None:
            self.x_prev = x
            self.t_prev = t
            return x

        t_e = t - self.t_prev
        if t_e <= 0.0:
            return x

        a_d = self.alpha(t_e, self.d_cutoff)
        dx = (x - self.x_prev) / t_e
        dx_hat = self.dx_prev + a_d * (dx - self.dx_prev)

        cutoff = self.min_cutoff + self.beta * abs(dx_hat)
        
        a = self.alpha(t_e, cutoff)
        x_hat = self.x_prev + a * (x - self.x_prev)

        # Guardar historial
        self.x_prev = x_hat
        self.dx_prev = dx_hat
        self.t_prev = t

        return x_hat

    def alpha(self, t_e, cutoff):
        r = 2 * math.pi * cutoff * t_e
        return r / (r + 1)