# Librerias
import subprocess
import sys

# Instalar librerías desde requirements.txt
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'Juegos/requirements.txt'])

from PyQt5 import QtWidgets, QtCore, QtGui
from TaTeTi.TaTeTi import TicTacToeUI
from Ahorcado.Ahorcado import AhorcadoUI
from PiedraPapelTijera.piedraPapelTijera import PiedraPapelTijeraUI

class MainMenu(QtWidgets.QWidget):
    def __init__(self):
        # Llamamos al contructor de la clase padre
        super().__init__()

        # Configuraciones de la ventana
        self.setWindowTitle("Menú Principal")
        self.setFixedSize(500, 400)
        self.setWindowIcon(QtGui.QIcon("Juegos/PiedraPapelTijera/Img/icon.png"))

        # Llamamos al método para inicializar la UI del juego
        self.initUI()

    # Método para inicializar la UI del juego
    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        # Crear el título del menú
        self.labelTitulo = QtWidgets.QLabel("Selecciona un juego:")
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setStyleSheet("font-size: 24px;  font-weight: bold; color: black;")
        layout.addWidget(self.labelTitulo)

        # Estilo aplicado a todos los botones
        buttonStyle = """
            QPushButton {
                font-family: "Arial";
                background-color: white;
                color: black;
                height: 60px;
                font-size: 18pt;
                border: 2px solid black;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: rgb(220, 220, 220);
            }
        """

        # Crear el botón del juego Ta-Te-Ti
        self.botonTaTeTi = QtWidgets.QPushButton("Ta-Te-Ti ❌⭕")
        self.botonTaTeTi.setStyleSheet(buttonStyle)
        self.botonTaTeTi.clicked.connect(self.lanzarTaTeTi)
        layout.addWidget(self.botonTaTeTi)

        # Crear el botón del juego Ahorcado
        self.botonAhorcado = QtWidgets.QPushButton("Ahorcado 😵")
        self.botonAhorcado.setStyleSheet(buttonStyle)
        self.botonAhorcado.clicked.connect(self.lanzarAhorcado)
        layout.addWidget(self.botonAhorcado)

        # Crear el botón del juego Piedra, Papel o Tijera
        self.botonPPT = QtWidgets.QPushButton("Piedra🪨, Papel📜 o Tijera ✂️")
        self.botonPPT.setStyleSheet(buttonStyle)
        self.botonPPT.clicked.connect(self.lanzarPPT)
        layout.addWidget(self.botonPPT)

        self.setLayout(layout)

    # Método para iniciar el juego Ta-Te-Ti
    def lanzarTaTeTi(self):
        self.taTeTi = TicTacToeUI(self)
        self.taTeTi.show()
        self.hide()

    # Método apara iniciar el juego Ahorcado
    def lanzarAhorcado(self):
        self.ahorcado = AhorcadoUI(self)
        self.ahorcado.show()
        self.hide()

    # Método apara iniciar el juego Piedra, Papel o Tijera
    def lanzarPPT(self):
        self.ppt = PiedraPapelTijeraUI(self)
        self.ppt.show()
        self.hide()

# Verifica si el módulo actual es el programa principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Crea una instancia de la aplicación Qt
    window = MainMenu() # Crea una instancia de la clase MainMenu
    window.show() # Muestra la ventana
    app.exec_() # Ejecuta la aplicación y espera a que termine