# Librerias
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class PiedraPapelTijeraIA:
    # Constructor
    def __init__(self):
        # Propiedades
        self.historialJugador = []
        self.historialIA = []
        self.entrenado = False
        self.jugadasNecesarias = 5 # Jugadas necesarias para entrenar a la IA

        # Inicialización del modelo de clasificación de Random Forest con 150 árboles aleatorios y utilizando todos los núcleos de CPU disponibles
        self.modelo = RandomForestClassifier(n_estimators=150, n_jobs=-1)

    def predecirJugada(self):
        # Si el modelo todavía no fue entrenado retorno aleatoriamente PIEDRA, PAPEL o TIJERA
        if not self.entrenado:
            return random.randint(1, 3)
        
        # Obtiene la ultimas 5 jugadas del historial del jugador
        ultimasJugadas = np.array(self.historialJugador[-self.jugadasNecesarias:]).reshape(1, -1)

        # Realiza una predicción de la siguiente jugada del jugador
        prediccion = self.modelo.predict(ultimasJugadas)[0]

        # Tupla para mejorar la legibilidad
        PIEDRA, PAPEL, TIJERA = 1, 2, 3

        # Retorna el valor que le ganaría al jugador depenediendo de la predicción realizada
        if prediccion == PIEDRA:
            return PAPEL
        elif prediccion == PAPEL:
            return TIJERA
        else:
            return PIEDRA 

    # Método para agregar la última jugada del jugador a su historial
    def registrarJugada(self, opJugador):
        self.historialJugador.append(opJugador)
        if len(self.historialJugador) > self.jugadasNecesarias:
            self.entrenarModelo()

    def entrenarModelo(self):
        # Crear una lista de jugadas del jugador
        X = [self.historialJugador[i : i + self.jugadasNecesarias] for i in range(len(self.historialJugador) - self.jugadasNecesarias)]
        
        # Crear una lista de las elecciones del jugador en base a sus jugadas previas
        Y = self.historialJugador[self.jugadasNecesarias:]
        
        # Entrenar el modelo utilizando las jugadas y las elecciones del jugador
        self.modelo.fit(X, Y)
        
        # Marcar el modelo como entrenado
        self.entrenado = True