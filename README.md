# Juegos Terminados

Para el correcto funcionamiento de los juegos, la carpeta que se debe abrir en Visual Studio es "Juegos terminados". Esto se debe a un problema con las rutas de los archivos.

## Ejecución del Programa

Para ejecutar el programa desde el menú principal, se debe ejecutar el archivo `main.py`. Las librerías necesarias se instalarán automáticamente al abrir el archivo `main.py`.

## Juegos Incluidos

### Ahorcado
La computadora elegirá una palabra al azar que el jugador deberá adivinar. La palabra aparecerá inicialmente como barras, mostrando el tamaño de la palabra. El jugador deberá arriesgar letras; si la letra se encuentra en la palabra, se mostrará al jugador. Por ejemplo, si la palabra es “sol”, en un inicio aparecerá como “_ _ _”, y si el usuario ingresa la letra “o”, aparecerá “_ o _”. Si el usuario ingresa una letra incorrecta, perderá uno de sus siete intentos. Si los intentos fallidos llegan a siete, el jugador habrá perdido. Si el usuario adivina todas las letras antes de agotar los intentos, habrá ganado.

### Ta-Te-Ti
Un jugador usa la X y el otro usa la O. El tablero tiene nueve casillas y los jugadores se turnan para colocarse en una de ellas. El objetivo es alinear tres de sus marcas en una fila, columna o diagonal para ganar. Si todas las casillas se llenan y nadie logra alinear tres marcas, el juego termina en empate.

### Piedra, Papel o Tijera
Permite que dos jugadores (un jugador humano y la computadora) elijan entre piedra, papel o tijera. Las reglas son: piedra gana a tijera, tijera gana a papel y papel gana a piedra.

## Implementaciones Generales

- Los juegos tienen una representación gráfica en la consola.
- Cada juego muestra el resultado de cada ronda, indicando quién ganó o si hubo empate.
- El puntaje total de cada jugador se registra y muestra después de cada ronda.
- Si el jugador ingresa una opción inválida, el programa muestra un mensaje de error adecuado.

## Mejoras y Especificaciones Adicionales

- Se implementó una interfaz gráfica utilizando la librería PyQt5.
- Se agregó un menú principal para seleccionar entre los juegos de "Ahorcado", "Ta-Te-Ti" y "Piedra, Papel o Tijera", cada uno con su propio menú de opciones.
- El juego de Ahorcado utiliza un archivo JSON con 428 palabras organizadas por dificultad: fácil (3-4 caracteres), normal (5-9 caracteres) y difícil (10+ caracteres). También muestra las letras acertadas e incorrectas que ya se han ingresado.
- El juego de Ta-Te-Ti tiene una IA con diferentes niveles de dificultad (fácil, normal, difícil) utilizando un algoritmo de aprendizaje por refuerzo que aprende de la experiencia.
- El juego de Piedra, Papel o Tijera tiene una IA que predice la siguiente jugada del jugador usando un clasificador de bosques aleatorios (Random Forest Classifier) basado en el historial del jugador.

¡Disfruta de los juegos!