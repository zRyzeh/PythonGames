import random

class Agent():
    # Constructor de la clase
    def __init__(self, game_class, epsilon=0.1, alpha=0.5, value_player="⭕"):
        # Propiedades
        self.V = {}
        self.NewGame = game_class
        self.epsilon = epsilon
        self.alpha = alpha
        self.value_player = value_player

    # Método para obtener la mejor jugada en formato state del tablero
    def getBestMove(self, game):
        allowed_state_values = self.__stateValues(game.allowedMoves())
        if game.player == self.value_player:
            return self.__argmaxV(allowed_state_values)
        return self.__randomV(allowed_state_values)

    # Método para obtener la mejor jugada en coordenadas
    def getBestMoveCoords(self, state):
        game = self.NewGame(state, player="⭕")
        bestMove = self.getBestMove(game)
        bestPosition = next(i for i in range(len(state)) if state[i] != bestMove[i])
        return divmod(bestPosition, 3)

    """
    --------------------------------------------------
    ------ Métodos para el aprendizaje de la IA ------
    --------------------------------------------------
    """

    # Método para aprender n episodios (los episodios son partidas)
    def learnGame(self, num_episodes=1000):
        for _ in range(num_episodes):
            self.learnFromEpisode()

    # Método para aprender de un episodio
    def learnFromEpisode(self):
        game = self.NewGame()
        move = self.learnSelectMove(game)[1]
        while move:
            move = self.learnFromMove(game, move)

    # Método para aprender de un movimiento
    def learnFromMove(self, game, move):
        game.makeMove(move)
        r = self.__reward(game)
        next_state_value = self.__stateValue(self.learnSelectMove(game)[0]) if game.isPlayable() else 0.0
        td_target = r + next_state_value
        current_state_value = self.__stateValue(move)
        self.V[move] = current_state_value + self.alpha * (td_target - current_state_value)
        return self.learnSelectMove(game)[1] if game.isPlayable() else None

    # Método para aprender del movimiento seleccionado en learnFromMove
    def learnSelectMove(self, game):
        allowed_state_values = self.__stateValues(game.allowedMoves())
        if game.player == self.value_player:
            best_move = self.__argmaxV(allowed_state_values)
        else:
            best_move = self.__argminV(allowed_state_values)

        selected_move = best_move
        if random.random() < self.epsilon:
            selected_move = self.__randomV(allowed_state_values)

        return (best_move, selected_move)

    # Métodos auxiliares para el aprendizaje de la IA
    def __stateValue(self, game_state):
        return self.V.get(game_state, 0.0)

    def __stateValues(self, game_states):
        return dict((state, self.__stateValue(state)) for state in game_states)

    def __argmaxV(self, state_values):
        max_V = max(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == max_V])
        return chosen_state

    def __argminV(self, state_values):
        min_V = min(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == min_V])
        return chosen_state

    def __randomV(self, state_values):
        return random.choice(list(state_values.keys()))

    def __reward(self, game):
        if game.winner == self.value_player:
            return 1.0
        elif game.winner:
            return -1.0
        return 0.0
    
    # Métodos para verificar el entrenamiento de la IA
    def demoGameStats(self):
        results = [self.demoGame() for _ in range(100000)]
        game_stats = {k: results.count(k) / 1000 for k in ["❌", "⭕", "-"]}
        print(f"  Resultados en porcentaje: {game_stats}")

    def demoGame(self):
        game = self.NewGame()
        while game.isPlayable():
            move = self.getBestMove(game)
            game.makeMove(move)
        if game.winner:
            return game.winner
        return "-"