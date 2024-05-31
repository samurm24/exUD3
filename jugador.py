import random

MAX_ENERGY = 100
MIN_ENERGY = 0


class Player:
    def __init__(self, idPlayer, nickname):
        self._idPlayer = idPlayer
        self._nickname = nickname
        self._energy = (MAX_ENERGY + MIN_ENERGY) // 2

    def get_idPlayer(self):
        return self._idPlayer

    def set_idPlayer(self, idPlayer):
        self._idPlayer = idPlayer

    def get_nickname(self):
        return self._nickname

    def set_nickname(self, nickname):
        self._nickname = nickname

    def get_energy(self):
        return self._energy

    def _set_energy(self, energy):
        if MIN_ENERGY <= energy <= MAX_ENERGY:
            self._energy = energy
        else:
            raise ValueError("Los valores deben estar entre MIN_ENERGY and MAX_ENERGY")

    def __str__(self):
        return f"[{self._idPlayer}, {self._nickname}, {self._energy}]"

    def boost(self, charge):
        if not isinstance(charge, int):
            charge = 0

        if charge < 0:
            charge = -charge

        carga = min(MAX_ENERGY - self._energy, charge)
        self._set_energy(self._energy + carga)

        return carga, self._energy
