# Librerias
from enum import Enum
import sys
import os
import pickle
from PyQt5 import QtWidgets, QtGui, QtCore
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Agrega TicTacToeGame y Agent al PYTHONPATH
from TicTacToeGame import TicTacToeGame

# Enum para las dificultades
class Dificultad(Enum):
    FACIL = 1
    NORMAL = 2
    DIFICIL = 3

class TicTacToeUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # Llamamos al contructor de la clase padre
        super().__init__()

        # Inicializar el juego
        self.game = TicTacToeGame()

        # Configuraciones de la ventana
        self.parent = parent
        self.setWindowTitle("Ta-Te-Ti")
        self.setFixedSize(500, 550)
        self.setWindowIcon(QtGui.QIcon("Juegos/TaTeTi/Img/icon.png"))

        # Llamamos al método para inicializar la UI del juego
        self.initUI()

        # Centrar la ventana
        fg = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(centerPoint)
        self.move(fg.topLeft())

        # Propiedades del juego
        self.turnPvP = "⭕"
        self.playerVictories = 0
        self.playerDefeats = 0
        self.drawIA = 0
        self.player1Victories = 0
        self.player2Victories = 0
        self.playersDraw = 0

    def initUI(self):
        # Inicialización y seteo de Layouts
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout) # Se setea al mainLayout como Layout principal
        self.stackedLayout = QtWidgets.QStackedLayout()
        self.mainLayout.addLayout(self.stackedLayout) # Se agrega el stackedLayout al mainLayout como Layout secundario

        # Creación y agregación de Widgets al stackedLayout
        self.mainMenu = self.createMainMenu()
        self.stackedLayout.addWidget(self.mainMenu)
        self.difficultyMenu = self.createDifficultyMenu()
        self.stackedLayout.addWidget(self.difficultyMenu)
        self.gameBoard = self.createGameBoard()
        self.stackedLayout.addWidget(self.gameBoard)

    # Método para crear el widget del menú principal
    def createMainMenu(self):
        widget = QtWidgets.QWidget()
        mainMenuLayout = QtWidgets.QVBoxLayout()
        imagesLayout = QtWidgets.QHBoxLayout()

        # Título
        title = QtWidgets.QLabel("Bienvenido al juego Ta-Te-Ti")
        title.setFont(QtGui.QFont("Impact", 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        mainMenuLayout.addWidget(title)

        # Añadir imagen de X
        labelX = QtWidgets.QLabel()
        pixmapX = QtGui.QPixmap("Juegos/TaTeTi/Img/X.png").scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        labelX.setPixmap(pixmapX)
        imagesLayout.addWidget(labelX, 0, QtCore.Qt.AlignLeft)
        
        # Añadir imagen de O
        labelO = QtWidgets.QLabel()
        pixmapO = QtGui.QPixmap("Juegos/TaTeTi/Img/O.png").scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        labelO.setPixmap(pixmapO)
        imagesLayout.addWidget(labelO, 0, QtCore.Qt.AlignRight)

        # Añadir el layout de imágenes al layout principal
        mainMenuLayout.addLayout(imagesLayout)

        # Botón Player vs IA
        btnPlayerVsIA = QtWidgets.QPushButton("Jugador contra IA 🤖")
        btnPlayerVsIA.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: white;
                color: black;
                height: 50px;
                font-size: 14pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
        """)
        btnPlayerVsIA.clicked.connect(lambda: self.stackedLayout.setCurrentWidget(self.difficultyMenu))
        mainMenuLayout.addWidget(btnPlayerVsIA)

        # Botón Player vs Player
        btnPlayerVsPlayer = QtWidgets.QPushButton("Jugador contra Jugador ⚔️")
        btnPlayerVsPlayer.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: white;
                color: black;
                height: 50px;
                font-size: 14pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
        """)
        btnPlayerVsPlayer.clicked.connect(self.startPvP)
        mainMenuLayout.addWidget(btnPlayerVsPlayer)

        # Botón para volver al menú principal
        btnExit = QtWidgets.QPushButton("Volver al menú principal 🌎")
        btnExit.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: white;
                color: black;
                height: 50px;
                font-size: 14pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
        """)
        btnExit.clicked.connect(self.goBack)
        mainMenuLayout.addWidget(btnExit)

        mainMenuLayout.setAlignment(QtCore.Qt.AlignCenter) # Alinear el menú al centro
        widget.setLayout(mainMenuLayout) # Setear el mainMenuLayout al widget

        return widget
    
    # Método para crear el widget del menú de dificultad
    def createDifficultyMenu(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Crear el título del menú
        title = QtWidgets.QLabel("Selecciona una dificultad")
        title.setFont(QtGui.QFont("Impact", 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        # Crear el botón de dificultad fácil
        btnEasy = QtWidgets.QPushButton("Fácil 😌")
        btnEasy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnEasy.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: rgb(50, 200, 30);;
                color: black;
                height: 50px;
                font-size: 16pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: green;
            }
        """)
        btnEasy.clicked.connect(lambda: self.startPvIA(Dificultad.FACIL))
        layout.addWidget(btnEasy)

        # Crear el botón de dificultad normal
        btnNormal = QtWidgets.QPushButton("Normal 🙂")
        btnNormal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnNormal.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: yellow;
                color: black;
                height: 50px;
                font-size: 16pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(200, 180, 0);
            }
        """)
        btnNormal.clicked.connect(lambda: self.startPvIA(Dificultad.NORMAL))
        layout.addWidget(btnNormal)

        # Crear el botón de dificultad difícil
        btnHard = QtWidgets.QPushButton("Difícil 😠")
        btnHard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnHard.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: red;
                color: black;
                height: 50px;
                font-size: 16pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(200, 25, 25);
            }
        """)
        btnHard.clicked.connect(lambda: self.startPvIA(Dificultad.DIFICIL))
        layout.addWidget(btnHard)

        # Crear el botón de volver al menú del juego
        btnBack = QtWidgets.QPushButton("Volver ↩️")
        btnBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnBack.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: white; 
                color: black;
                height: 40px;
                font-size: 14pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
        """)
        btnBack.clicked.connect(lambda: self.stackedLayout.setCurrentWidget(self.mainMenu))
        layout.addWidget(btnBack)

        # Alineamos los elementos al centro y seteamos el layout al widget del menú de dificultad
        layout.setAlignment(QtCore.Qt.AlignCenter)
        widget.setLayout(layout)

        return widget

    # Método para crear el widget del tablero de juego
    def createGameBoard(self):
        widget = QtWidgets.QWidget()
        self.boardLayout = QtWidgets.QVBoxLayout()

        # Label para mostrar los contadores de victorias, empates y derrotas
        self.lblStatus = QtWidgets.QLabel()
        self.lblStatus.setFont(QtGui.QFont("Arial", 14))
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.boardLayout.addWidget(self.lblStatus)

        # Label para mostrar el turno de cada jugador
        self.lblTurn = QtWidgets.QLabel()
        self.lblTurn.setFont(QtGui.QFont("Arial", 20))
        self.lblTurn.setAlignment(QtCore.Qt.AlignCenter)
        self.boardLayout.addWidget(self.lblTurn)

        # Grid para mostrar el tablero
        self.gridLayout = QtWidgets.QGridLayout()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = QtWidgets.QPushButton(" ")
                button.setFont(QtGui.QFont("Helvetica", 24))
                button.setFixedSize(100, 100)

                """
                En PyQt5, r=row y c=col están capturando los valores actuales 
                de row y col en el momento de la conexión de la señal, para que cuando se haga clic
                en el botón, esos valores se pasen correctamente a la función.
                """
                button.clicked.connect(lambda _, r=row, c=col: self.makeMove(r, c))

                self.gridLayout.addWidget(button, row, col)
                self.buttons[row][col] = button
        self.boardLayout.addLayout(self.gridLayout)

        # Botón para volver al menú del juego
        self.btnBack = QtWidgets.QPushButton("Volver ↩️")
        self.btnBack.setStyleSheet("""
            QPushButton {
                font-family: "Arial";
                background-color: white;
                color: black;
                height: 40px;
                font-size: 14pt;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
        """)
        self.btnBack.clicked.connect(self.backToMenu)
        self.boardLayout.addWidget(self.btnBack)

        widget.setLayout(self.boardLayout)
        return widget
    
    """
    ----------------------------------------------------------------------------
    ----- Métodos para manejar la lógica del juego con la interfaz gráfica -----
    ----------------------------------------------------------------------------
    """

    # Método para jugar al modo Jugador contra Jugador
    def startPvP(self):
        self.changeTurn()
        self.game = TicTacToeGame(player=self.turnPvP)
        self.game.gameMode = "PvP"
        self.updateStatus()
        self.stackedLayout.setCurrentWidget(self.gameBoard)
        self.updateBoard()

    # Método para jugar al modo Jugador contra IA
    def startPvIA(self, difficulty):
        self.game = TicTacToeGame(player="❌")
        self.game.gameMode = "PvIA"
        self.game.difficulty = difficulty
        self.updateStatus()
        self.stackedLayout.setCurrentWidget(self.gameBoard)
        self.updateBoard()
        if difficulty == Dificultad.DIFICIL:
            self.game.player = "⭕"
            self.moveIA()

    # Método para realizar un movimiento
    def makeMove(self, row, col):
        if self.game.getElementWithCoords(row, col) == " ":
            nextState = self.game.getNextStateWithCoords(row, col)
            self.game.makeMove(nextState)
            self.updateBoard()
            winner = self.game.verifyWinner()
            if winner:
                if self.game.gameMode == "PvIA":
                    self.playerVictories += 1
                    QtWidgets.QMessageBox.information(self, "Fin del juego", f"¡Ganaste! 🥳")
                    self.startPvIA(self.game.difficulty)
                else:
                    if winner == "❌":
                        self.player1Victories += 1
                    else:
                        self.player2Victories += 1
                    QtWidgets.QMessageBox.information(self, "Fin del juego", f"Jugador {winner} gana 🥳")
                    self.startPvP()
            elif self.game.isFullBoard():
                if self.game.gameMode == "PvIA":
                    self.drawIA += 1
                    QtWidgets.QMessageBox.information(self, "Fin del juego", "Es un empate 😁🤝🤖")
                    self.startPvIA(self.game.difficulty)
                else:
                    self.playersDraw += 1
                    QtWidgets.QMessageBox.information(self, "Fin del juego", "Es un empate 😃🤝😁")
                    self.startPvP()
            elif self.game.gameMode == "PvIA":
                self.disableBoard()
                QtCore.QTimer.singleShot(500, lambda: self.moveIA()) 

    # Método para realizar un movimiento de la IA
    def moveIA(self):
        if self.game.difficulty == Dificultad.FACIL:
            row, col = self.game.randomMovement()
        else:
            with open(f"Juegos/TaTeTi/IA/agent{self.game.difficulty.name.capitalize()}.pkl", "rb") as f:
                agent = pickle.load(f)
            row, col = agent.getBestMoveCoords(self.game.state)

        nextState = self.game.getNextStateWithCoords(row, col)
        self.game.makeMove(nextState)
        self.updateBoard()

        winner = self.game.verifyWinner()
        if winner:
            self.playerDefeats += 1
            QtWidgets.QMessageBox.information(self, "Fin del juego", "Derrota 😢. La IA ha ganado 🤖")
            self.startPvIA(self.game.difficulty)
        elif self.game.isFullBoard():
            self.drawIA += 1
            QtWidgets.QMessageBox.information(self, "Fin del juego", "Es un empate 😁🤝🤖")
            self.startPvIA(self.game.difficulty)
        self.enableBoard()

    # Método para actualizar el tablero del juego
    def updateBoard(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText(self.game.getElementWithCoords(row, col))
        self.updateStatus()

    # Método para actualizar el estado del juego
    def updateStatus(self):
        if self.game.gameMode == "PvIA":
            self.lblStatus.setText(f"Victorias 🥳: {self.playerVictories}\nEmpates 😁🤝🤖: {self.drawIA}\nDerrotas 🤖: {self.playerDefeats}")
        else:
            self.lblStatus.setText(f"Jugador ❌: {self.player1Victories}\nJugador ⭕: {self.player2Victories}\nEmpates 😃🤝😁: {self.playersDraw}")

        player = self.game.getCurrentPlayer()
        if player != None:
            self.lblTurn.setText(f"Turno de {player}")
        self.setWindowTitle("Ta-Te-Ti" if player is None else f"Ta-Te-Ti - Turno de {player}")

    # Método para deshabilitar los botones del tablero
    def disableBoard(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setEnabled(False)

    # Método para habilitar los botones del tablero
    def enableBoard(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setEnabled(True)

    # Método para cambiar el turno del jugador actual en el modo PvP
    def changeTurn(self):
        self.turnPvP = "❌" if self.turnPvP == "⭕" else "⭕"

    # Método para volver al menú del juego
    def backToMenu(self):
        self.stackedLayout.setCurrentWidget(self.mainMenu)
    
    # Método para volver al menú principal
    def goBack(self):
        self.close()
        if self.parent:
            self.parent.show()

    # Evento que se ejecuta al cerrar la ventana
    def closeEvent(self, event):
        QtWidgets.QMessageBox.information(self, "Despedida", "¡Gracias por jugar al Ta-Te-Ti!")

# Verifica si el módulo actual es el programa principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Crea una instancia de la aplicación Qt
    window = TicTacToeUI() # Crea una instancia de la clase TicTacToeUI
    window.show() # Muestra la ventana
    app.exec_() # Ejecuta la aplicación y espera a que termine