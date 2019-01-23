import unittest
import game as g

class TestUpdateScore(unittest.TestCase):

    def test_game(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("quit"), -1)