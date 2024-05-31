import unittest
from jugador import Player
from jugador import MIN_ENERGY
from jugador import MAX_ENERGY
from game import Game



class Test(unittest.TestCase):
    def test1(self):
        p1 = Player(1, 'a')
        self.assertEqual(p1.get_energy(), 50)

    def test2(self):
        p1 = Player(1, 'a')
        p1.boost(-100)
        self.assertTrue(p1.get_energy() >= MIN_ENERGY)

    def test3(self):
        p1 = Player(1, 'a')
        p1.boost(200)
        self.assertTrue(p1.get_energy() <= MAX_ENERGY)

    def test4(self):
        p1 = Player(1, 'a')
        p2 = Player(2, 'b')
        p1.boost(50)
        p2.boost(75)
        winner = Game(p1, p2, 3).winner()
        self.assertIsNotNone(winner)

