# Librerias
import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Agregar PiedraPapelTijeraGame al PYTHONPATH
from PiedraPapelTijeraGame import PiedraPapelTijeraGame

class PiedraPapelTijeraUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # Llamamos al contructor de la clase padre
        super().__init__()

        # Inicializar el juego
        self.game = PiedraPapelTijeraGame()

        # Configuraciones de la ventana
        self.parent = parent
        self.setWindowTitle("Piedra, Papel o Tijera")
        self.setFixedSize(600, 550)
        self.setWindowIcon(QtGui.QIcon("Juegos/PiedraPapelTijera/Img/icon.png"))

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
        self.setLayout(self.mainLayout)  # Se setea al mainLayout como Layout principal
        self.stackedLayout = QtWidgets.QStackedLayout()
        self.mainLayout.addLayout(self.stackedLayout)  # Se agrega el stackedLayout al mainLayout como Layout secundario

        # Creación y agregación de Widgets al stackedLayout
        self.mainMenu = self.createMainMenu()
        self.stackedLayout.addWidget(self.mainMenu)
        self.gameMenu = self.createGameMenu()
        self.stackedLayout.addWidget(self.gameMenu)

    # Método para crear el widget del menú principal
    def createMainMenu(self):
        widget = QtWidgets.QWidget()
        mainMenuLayout = QtWidgets.QVBoxLayout()
        imagesLayout = QtWidgets.QHBoxLayout()

        # Título
        title = QtWidgets.QLabel("Bienvenido al juego Piedra, Papel o Tijera")
        title.setFont(QtGui.QFont("Impact", 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        mainMenuLayout.addWidget(title)

        # Añadir imagen de Piedra, Papel, Tijera como decoración
        labelPiedra = QtWidgets.QLabel()
        pixmapPiedra = QtGui.QPixmap("Juegos/PiedraPapelTijera/Img/stone.png").scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        labelPiedra.setPixmap(pixmapPiedra)
        imagesLayout.addWidget(labelPiedra, 0, QtCore.Qt.AlignLeft)

        labelPapel = QtWidgets.QLabel()
        pixmapPapel = QtGui.QPixmap("Juegos/PiedraPapelTijera/Img/paper.png").scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        labelPapel.setPixmap(pixmapPapel)
        imagesLayout.addWidget(labelPapel, 0, QtCore.Qt.AlignCenter)

        labelTijera = QtWidgets.QLabel()
        pixmapTijera = QtGui.QPixmap("Juegos/PiedraPapelTijera/Img/scissor.png").scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        labelTijera.setPixmap(pixmapTijera)
        imagesLayout.addWidget(labelTijera, 0, QtCore.Qt.AlignRight)

        # Añadir el layout de imágenes al layout principal
        mainMenuLayout.addLayout(imagesLayout)

        # Botón Jugar contra IA
        btnJugar = QtWidgets.QPushButton("Jugar contra IA 🤖")
        btnJugar.setStyleSheet("""
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
        btnJugar.clicked.connect(lambda: self.stackedLayout.setCurrentWidget(self.gameMenu))
        mainMenuLayout.addWidget(btnJugar)

        # Botón Volver al menú principal
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

        mainMenuLayout.setAlignment(QtCore.Qt.AlignCenter)  # Alinear el menú al centro
        widget.setLayout(mainMenuLayout)  # Setear el mainMenuLayout al widget

        return widget

    def createGameMenu(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Label para mostrar los contadores de victorias, empates y derrotas
        self.lblStatus = QtWidgets.QLabel(f"Victorias 🥳: 0\nEmpates 😁🤝🤖: 0\nDerrotas 🤖: 0")
        self.lblStatus.setFont(QtGui.QFont("Arial", 14))
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus)

        # Label para solicitar al usuario que ingrese una opción
        labelTitulo = QtWidgets.QLabel("Selecciona una opción:")
        labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        labelTitulo.setFont(QtGui.QFont("Impact", 20))
        layout.addWidget(labelTitulo)

        # Creación de un layout horizontal para los botones de opciones
        opcionesLayout = QtWidgets.QHBoxLayout()

        # Botón para la opción PIEDRA 
        botonPiedra = QtWidgets.QPushButton()
        iconPiedra = QtGui.QIcon("Juegos/PiedraPapelTijera/Img/stone.png")
        botonPiedra.setIcon(iconPiedra)
        botonPiedra.setIconSize(QtCore.QSize(100, 100))
        botonPiedra.setFixedSize(120, 120)
        botonPiedra.clicked.connect(lambda: self.playGame(1))
        opcionesLayout.addWidget(botonPiedra)

        # Botón para la opción PAPEL 
        botonPapel = QtWidgets.QPushButton()
        iconPapel = QtGui.QIcon("Juegos/PiedraPapelTijera/Img/paper.png")
        botonPapel.setIcon(iconPapel)
        botonPapel.setIconSize(QtCore.QSize(100, 100))
        botonPapel.setFixedSize(120, 120)
        botonPapel.clicked.connect(lambda: self.playGame(2))
        opcionesLayout.addWidget(botonPapel)

        # Botón para la opción TIJERA 
        botonTijera = QtWidgets.QPushButton()
        iconTijera = QtGui.QIcon("Juegos/PiedraPapelTijera/Img/scissor.png")
        botonTijera.setIcon(iconTijera)
        botonTijera.setIconSize(QtCore.QSize(100, 100))
        botonTijera.setFixedSize(120, 120)
        botonTijera.clicked.connect(lambda: self.playGame(3))
        opcionesLayout.addWidget(botonTijera)

        # Agregar al layout principal el opcionesLayout
        layout.addLayout(opcionesLayout)

        # Botón para volver al menú principal
        btnVolver = QtWidgets.QPushButton("Volver ↩️")
        btnVolver.setStyleSheet("""
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
        btnVolver.clicked.connect(lambda: self.stackedLayout.setCurrentWidget(self.mainMenu))
        layout.addWidget(btnVolver)

        layout.setAlignment(QtCore.Qt.AlignCenter)  # Alinear el layout al centro
        widget.setLayout(layout)  # Setear el layout al widget

        return widget

    # Método para manejar la lógica del juego con la interfaz gráfica
    def playGame(self, opJugador):
        # Llama al método jugar del objeto game enviandole como para metro la opción elegida por el jugador
        opJugador, opIA, resultado = self.game.jugar(opJugador)

        # Diccionario para mejorar la legibilidad
        opciones = { 
            1: "Piedra 🪨",
            2: "Papel 📜",
            3: "Tijera ✂️"
        }

        self.lblStatus.setText(f"Victorias 🥳: {self.game.victorias}\nEmpates 😁🤝🤖: {self.game.empates}\nDerrotas 🤖: {self.game.derrotas}")
        QtWidgets.QMessageBox.information(self, "Resultado", f"Seleccionaste {opciones[opJugador]}\nLa IA seleccionó {opciones[opIA]}.\n\n          {resultado}")

    # Método para volver al menú principal
    def goBack(self):
        self.close()
        if self.parent:
            self.parent.show()
    
        # Evento que se ejecuta al cerrar la ventana
    def closeEvent(self, event):
        QtWidgets.QMessageBox.information(self, "Despedida", "¡Gracias por jugar al Piedra, Papel o Tijera!")

# Verifica si el módulo actual es el programa principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Crea una instancia de la aplicación Qt
    window = PiedraPapelTijeraUI() # Crea una instancia de la clase PiedraPapelTijeraUI
    window.show() # Muestra la ventana
    app.exec_() # Ejecuta la aplicación y espera a que termine