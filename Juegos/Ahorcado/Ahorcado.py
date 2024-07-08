# Librerias
from PyQt5 import QtWidgets, QtGui, QtCore
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Agregar AhorcadoGame al PYTHONPATH
from AhorcadoGame import AhorcadoGame
from enum import Enum

# Enum para la dificultad
class Dificultad(Enum):
    FACIL = "facil"
    NORMAL = "normal"
    DIFICIL = "dificil"

class AhorcadoUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # Llamamos al contructor de la clase padre
        super().__init__()

        # Inicializar el juego
        self.game = AhorcadoGame()

        # Configuraciones de la ventana
        self.parent = parent
        self.setWindowTitle("Ahorcado")
        self.setFixedSize(500, 700)
        self.setWindowIcon(QtGui.QIcon("Juegos/Ahorcado/Img/icon.png"))

        # Llamamos al método para inicializar la UI del juego
        self.initUI()

        # Centrar la ventana
        fg = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(centerPoint)
        self.move(fg.topLeft())

    # Método para inicializar la UI del juego
    def initUI(self):
        # Inicialización y seteo de Layouts
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout) # Se setea al mainLayout como Layout principal
        self.stackedLayout = QtWidgets.QStackedLayout()
        self.mainLayout.addLayout(self.stackedLayout)  # Se agrega el stackedLayout al mainLayout como Layout secundario

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

        # Crear el título del menú
        title = QtWidgets.QLabel("Bienvenido al juego Ahorcado")
        title.setFont(QtGui.QFont("Impact", 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        mainMenuLayout.addWidget(title)

        # Crear el botón de jugar
        btnPlay = QtWidgets.QPushButton("Jugar 🎮")
        btnPlay.setStyleSheet("""
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
        btnPlay.clicked.connect(lambda: self.stackedLayout.setCurrentWidget(self.difficultyMenu))
        mainMenuLayout.addWidget(btnPlay)

        # Crear el botón de volver al menú principal
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

        # Alineamos los elementos al centro y seteamos el layout mainMenuLayout al widget del menú 
        mainMenuLayout.setAlignment(QtCore.Qt.AlignCenter)
        widget.setLayout(mainMenuLayout)

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
        btnEasy.clicked.connect(lambda: self.startGame(Dificultad.FACIL))
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
        btnNormal.clicked.connect(lambda: self.startGame(Dificultad.NORMAL))
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
        btnHard.clicked.connect(lambda: self.startGame(Dificultad.DIFICIL))
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

        # Crear el texto del estado del juego
        self.lblStatus = QtWidgets.QLabel(f"Victorias 🥳: 0\nDerrotas 😢: 0")
        self.lblStatus.setFont(QtGui.QFont("Arial", 16))
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.boardLayout.addWidget(self.lblStatus)

        # Crear el texto de las letras incorrectas
        self.lblIncorrectas = QtWidgets.QLabel("Letras incorrectas: ")
        self.lblIncorrectas.setFont(QtGui.QFont("Arial", 16))
        self.lblIncorrectas.setAlignment(QtCore.Qt.AlignCenter)
        self.boardLayout.addWidget(self.lblIncorrectas)

        # Crear el espacio donde se mostrará la imagen del ahorcado
        self.lblAhorcado = QtWidgets.QLabel()
        self.lblAhorcado.setAlignment(QtCore.Qt.AlignCenter)
        self.boardLayout.addWidget(self.lblAhorcado)

        # Crear el texto de la palabra eligida
        self.lblPalabra = QtWidgets.QLabel()
        self.lblPalabra.setFont(QtGui.QFont("Arial", 20))
        self.lblPalabra.setAlignment(QtCore.Qt.AlignCenter)
        self.boardLayout.addWidget(self.lblPalabra)

        # Crear el input donde se ingresará la letra a adivinar
        self.inputLetra = QtWidgets.QLineEdit()
        self.inputLetra.setFont(QtGui.QFont("Arial", 20))
        self.inputLetra.setMaxLength(1)
        self.inputLetra.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLetra.setFixedWidth(100)
        self.inputLetra.returnPressed.connect(self.checkLetra)
        self.boardLayout.addWidget(self.inputLetra, alignment=QtCore.Qt.AlignCenter)

        # Crear el botón para adivinar la letra
        self.btnAdivinar = QtWidgets.QPushButton("Adivinar")
        self.btnAdivinar.setFont(QtGui.QFont("Arial", 14))
        self.btnAdivinar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdivinar.setStyleSheet("""
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
        self.btnAdivinar.clicked.connect(self.checkLetra)
        self.boardLayout.addWidget(self.btnAdivinar)

        # Crear el botón para volver al menú del juego
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
        self.boardLayout.addWidget(btnBack)

        # Alineamos los elementos al centro y seteamos el layout al widget del tablero del juego
        self.boardLayout.setAlignment(QtCore.Qt.AlignCenter)
        widget.setLayout(self.boardLayout)

        return widget
    
    """
    ----------------------------------------------------------------------------
    ----- Métodos para manejar la lógica del juego con la interfaz gráfica -----
    ----------------------------------------------------------------------------
    """

    # Método para iniciar un nuevo juego
    def startGame(self, dificultad):
        self.game.iniciarJuego(dificultad)
        self.updateGameBoard()
        self.stackedLayout.setCurrentWidget(self.gameBoard)

    # Método para actualizar el tablero del juego
    def updateGameBoard(self):
        self.lblAhorcado.setPixmap(QtGui.QPixmap(f"Juegos/Ahorcado/Img/ahorcado{self.game.intentosFallidos}.png")
            .scaled(300, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.lblPalabra.setText(" ".join(self.game.letrasEncontradas))
        self.lblStatus.setText(f"Victorias 🥳: {self.game.victorias}\nDerrotas 😢: {self.game.derrotas}")
        self.lblIncorrectas.setText(f"Letras incorrectas: {', '.join(self.game.letrasIncorrectas)}")

    # Método para verificar si una letra se encuentra en la palabra elegida
    def checkLetra(self):
        # Obtenemos la letra del input
        letra = self.inputLetra.text().upper()

        if not letra.isalpha():
            QtWidgets.QMessageBox.warning(self, "Caracter inválido", "Por favor, ingresa una letra del abecedario.")
            self.inputLetra.clear()
            return

        if letra in self.game.letrasEncontradas:
            QtWidgets.QMessageBox.information(self, "Letra ya adivinada", f"Ya has adivinado la letra '{letra}' anteriormente.")
        elif letra in self.game.letrasIncorrectas:
            QtWidgets.QMessageBox.information(self, "Letra incorrecta repetida", f"Ya has ingresado la letra incorrecta '{letra}' anteriormente.")
        else: 
            self.game.adivinarLetra(letra)
            
        self.inputLetra.clear()
        self.updateGameBoard()

        if self.game.estaPerdido():
            self.game.derrotas += 1
            QtWidgets.QMessageBox.information(self, "Fin del juego", f"Perdiste! La palabra era {self.game.palabraElegida}")
            self.startGame(self.game.dificultadActual)
        elif self.game.estaGanado():
            self.game.victorias += 1
            QtWidgets.QMessageBox.information(self, "Fin del juego", "Ganaste! Adivinaste la palabra")
            self.startGame(self.game.dificultadActual)

    # Método para volver al menú principal
    def goBack(self):
        self.close()
        if self.parent:
            self.parent.show()

    # Evento que se ejecuta al cerrar la ventana
    def closeEvent(self, event):
        QtWidgets.QMessageBox.information(self, "Despedida", "¡Gracias por jugar al Ahorcado!")
        
# Verifica si el módulo actual es el programa principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Crea una instancia de la aplicación Qt
    window = AhorcadoUI() # Crea una instancia de la clase AhorcadoUI
    window.show() # Muestra la ventana
    app.exec_() # Ejecuta la aplicación y espera a que termine