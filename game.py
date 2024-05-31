import random


class Game:
    def __init__(self, player1, player2, rounds):
        self._player1 = player1
        self._player2 = player2
        self._rounds = rounds

    def playRound(self):
        carga_player1 = random.randint(-25, 25)
        carga_player2 = random.randint(-25, 25)

        fuerza_aplicada_player1, energia_player1 = self._player1.boost(carga_player1)
        fuerza_aplicada_player2, energia_player2 = self._player2.boost(carga_player2)

        return [(fuerza_aplicada_player1, energia_player1), (fuerza_aplicada_player2, energia_player2)]

    def winner(self):
        ganador=""
        if self._player1.get_energy() > self._player2.get_energy():
            ganador = self._player1
        elif self._player2.get_energy() > self._player1.get_energy():
            ganador = self._player2
        return ganador


    def play(self):
        for i in range(self._rounds):
            result = self.playRound()
            print(f"Round {i + 1}: {result}")


        return self.winner()

