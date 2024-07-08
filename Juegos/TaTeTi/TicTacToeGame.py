# Librerias
import random

class TicTacToeGame():
    # Constructor
    def __init__(self, state = "         ", player = "⭕", gameMode = None):
        # Propiedades
        self.state = state
        self.player = player
        self.winner = None
        self.difficulty = None
        self.gameMode = gameMode

    # Método para realizar un movimiento en el tablero
    def makeMove(self, nextState):
        self.state = nextState
        self.winner = self.verifyWinner()
        self.player = None if self.winner else ("⭕" if self.player == "❌" else "❌")
    
    # Método para verificar si el tablero está completo
    def isFullBoard(self):
        return all([element != " " for element in self.state])

    # Método para verificar si hay un ganador
    def verifyWinner(self):
        # Lista con posibles victorias
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontales
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticales
                (0, 4, 8), (2, 4, 6)]             # Diagonales
        
        # Recorro cada linea de las posibles victorias
        for line in lines:
            # Si todos los elementos de cada linea del tablero son iguales y distintos de " "
            if self.state[line[0]] == self.state[line[1]] == self.state[line[2]] != " ": 
                return self.state[line[0]] # Retorna el jugador, el cual ganó el juego
        return None # En caso de que ninguno de los jugadores hayan completado al menos una linea retorna None
    
    # Obtiene un elemento del tablero a partir de unas coordenadas
    def getElementWithCoords(self, row, col):
        return self.state[row*3 + col]
    
    # Obtiene el proximo estado del tablero a partir de unas coordenadas
    def getNextStateWithCoords(self, row, col):
        i = row*3 + col
        nextState = self.state[:i] + self.player + self.state[i+1:]
        return nextState
    
    # Obtiene el jugador actual
    def getCurrentPlayer(self):
        return self.player

    # Método para obtener un movimiento aleatorio disponible del tablero
    def randomMovement(self):
        # Crea una lista con los movimientos disponibles en coordenadas,
        # divmod divide i por 3 y devuelve una tupla donde el primer elemento será el cociente y el segundo el resto
        movements = [divmod(i, 3) for i in range(9) if self.state[i] == " "]
        return random.choice(movements) # Retorna de forma aleatoria uno de los elementos disponibles
    
    """
    ------------------------------------------------------------
    ------ Métodos que solo se utilizan en la clase Agent ------
    ------------------------------------------------------------
    """

    # Método para obtener una lista con los movimientos posibles en formato state
    def allowedMoves(self):
        return [ self.state[:i] + self.player + self.state[i+1:] 
            for i in range(len(self.state)) 
                if self.state[i] == " " ]

    # Método para verificar si el juego es jugable
    def isPlayable(self):
        return not self.winner and any(self.allowedMoves())