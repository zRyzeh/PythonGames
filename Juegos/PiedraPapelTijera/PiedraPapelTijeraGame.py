# Librerias
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Agregar PiedraPapelTijeraIA al PYTHONPATH
from PiedraPapelTijeraIA import PiedraPapelTijeraIA

class PiedraPapelTijeraGame:
    # Constructor
    def __init__(self):
        # Propiedades del juego
        self.ia = PiedraPapelTijeraIA()
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0

    # Método para jugar
    def jugar(self, opJugador):
        opIA = self.ia.predecirJugada() # Obtiene la predicción de la IA
        resultado = self.determinarGanador(opJugador, opIA) # Obtiene el ganador
        self.ia.registrarJugada(opJugador) # Registra la jugada del jugador para entrenar a la IA

        if resultado == "Victoria 🥳":
            self.victorias += 1
        elif resultado == "Empate 😄":
            self.empates += 1
        else:
            self.derrotas += 1

        return opJugador, opIA, resultado

    # Función para determinar el ganador
    def determinarGanador(self, opJugador, opIA):
        if opJugador == opIA: # Si las elecciones de la IA y el jugador son iguales es un empate
            return "Empate 😄"
        
        # Tupla para mejorar la legibilidad
        PIEDRA, PAPEL, TIJERA = 1, 2, 3

        # Diccionario de posibles victorias del jugador
        resultados = {
            (PIEDRA, TIJERA): "Victoria 🥳",
            (PAPEL, PIEDRA): "Victoria 🥳",
            (TIJERA, PAPEL): "Victoria 🥳"
        }

        # Si se encuentra la tupla (opJugador, opIA) retorna "Victoria 🥳", en caso contrario retorna "Derrota 😥"
        return resultados.get((opJugador, opIA), "Derrota 😥")