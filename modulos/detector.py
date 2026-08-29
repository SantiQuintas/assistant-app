import mediapipe as mp
import cv2 as cv
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

class DetectorManos:
    mp_manos = None
    mp_dibujo = None
    manos = None

    def __init__(self):
        self.mp_manos = hands
        self.mp_dibujo = drawing_utils
        self.manos = self.mp_manos.Hands(static_image_mode = False, max_num_hands = 2, min_detection_confidence=0.7, min_tracking_confidence=0.7) 
        
    def encontrar_manos(self, frame):
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        resultados = self.manos.process(frame_rgb)
        alto, ancho, canales = frame.shape
        posiciones = []
        if resultados.multi_hand_landmarks:
            for mano in resultados.multi_hand_landmarks:
                self.mp_dibujo.draw_landmarks(frame, mano, self.mp_manos.HAND_CONNECTIONS)
                for id, landmark in enumerate(mano.landmark):
                    posicion = []
                    posicion.append(id)
                    posicion.append(int(landmark.x * ancho))
                    posicion.append(int(landmark.y * alto))
                    posiciones.append(posicion)

        return frame,posiciones
    