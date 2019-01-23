import unittest
import game as g

class TestParseUserInput(unittest.TestCase):

    def test_quit(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("quit"), -1)

    def test_gibberish(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("aasdfh@2348"), 0)

    def test_nocomma(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("12"), 0)

    def test_badspare(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input(",/"), 0)

    def test_greaterthanten(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("8,9"), 0)

    def test_strike(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("X"), 1)

    def test_spare(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("2,/"), 1)

    def test_openframe(self):
        game = g.Game("test")
        self.assertEqual(game.parse_user_input("2,4"), 1)

    def test_tenthframe1(self):
        game = g.Game("test")
        game.frame = 9
        self.assertEqual(game.parse_user_input("X,X,X"), 1)

    def test_tenthframe2(self):
        game = g.Game("test")
        game.frame = 9
        self.assertEqual(game.parse_user_input("6,/,X"), 1)

    def test_tenthframe3(self):
        game = g.Game("test")
        game.frame = 9
        self.assertEqual(game.parse_user_input("X, 1, 1"), 1)

    def test_tenthframe4(self):
        game = g.Game("test")
        game.frame = 8
        self.assertEqual(game.parse_user_input("X, 1, 1"), 0)