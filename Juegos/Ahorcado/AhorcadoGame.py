import random
import json

# Carga el archivo palabrasAhorcadoOrganizadas.json en la variable palabrasJSON
with open("Juegos/Ahorcado/palabrasAhorcadoOrganizadas.json", "r", encoding="utf-8") as file:
    palabrasJSON = json.load(file)

class AhorcadoGame:
    # Constructor
    def __init__(self):
        # Inicializacion de parametros
        self.intentosFallidos = 0
        self.palabraElegida = ""
        self.letrasEncontradas = []
        self.letrasIncorrectas = []
        self.dificultadActual = None
        self.victorias = 0
        self.derrotas = 0

    # Método para iniciar un nuevo juego
    def iniciarJuego(self, dificultad):
        self.intentosFallidos = 0
        self.dificultadActual = dificultad

        # Obtiene una palabra al azar de palabrasJSON dependiendo de la dificultad y la transforma a mayúsculas
        self.palabraElegida = random.choice(palabrasJSON[dificultad.value]).upper()

        self.letrasEncontradas = ["_"] * len(self.palabraElegida)
        self.letrasIncorrectas = []

    # Método para adivinar una letra
    def adivinarLetra(self, letra):
        if letra in self.letrasEncontradas or letra in self.letrasIncorrectas:
            return

        if letra in self.palabraElegida:
            for i, char in enumerate(self.palabraElegida): # Recorre cada letra de palabras elegidas, obteniendo su indice y valor
                if char == letra: # Si la letra de la palabra elegida es igual a la letra recorrida
                    self.letrasEncontradas[i] = letra # Reemplazo el valor de la lista letrasEncontradas[i] por la letra
                    """
                    Ej: Si palabraElegida es "PERRO", letrasEncontradas en un inicio es ["_", "_", "_", "_", "_"]. 
                    Si la letra a adivinar es "R", al recorrer el for, reemplazara el indice 2 y 3 de letrasEncontradas por una "R": 
                    letrasEncontradas = ["_", "_", "R", "R", "_"]
                    """
        else:
            self.letrasIncorrectas.append(letra)
            self.intentosFallidos += 1

    def estaGanado(self):
        return "_" not in self.letrasEncontradas

    def estaPerdido(self):
        return self.intentosFallidos >= 7