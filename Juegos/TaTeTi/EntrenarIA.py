# Librerias
import pickle
from Agent import Agent
from TicTacToeGame import TicTacToeGame 

# Inicializar instancia de la clase Agent
agent = Agent(TicTacToeGame, epsilon=0.1, alpha=0.5, value_player="⭕")

# Antes de aprender
print("Antes de aprender:")
agent.demoGameStats()

# Entrenamiento del agente
print("Después de aprender 50.000 partidas:")
agent.learnGame(50000)
agent.demoGameStats()

# Guardar IA nivel normal
with open("agentNormal.pkl", "wb") as f:
    pickle.dump(agent, f)

# Entrenamiento del agente
print("Después de aprender 100.000 partidas:")
agent.learnGame(100000)
agent.demoGameStats()

# Verificar si puede resolver el probelma de ejemplo
state = " ❌❌ ⭕   ⭕"
move = agent.getBestMoveCoords(state)
print("Predicción", move)

# Guardar IA nivel difícil
with open("agentDificil.pkl", "wb") as f:
    pickle.dump(agent, f)