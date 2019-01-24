import unittest
import game as g


#tests scoring algorithm

class TestUpdateScore(unittest.TestCase):

    def test_one_frame1(self):
        game = g.Game("test")
        game.frame_input = ['X']
        game.add_frame()
        self.assertEqual(game.runningScore, 0)

    def test_one_frame2(self):
        game = g.Game("test")
        game.frame_input = ['1','/']
        game.add_frame()
        self.assertEqual(game.runningScore, 0)

    def test_one_frame3(self):
        game = g.Game("test")
        game.frame_input = ['1', '3']
        game.add_frame()
        self.assertEqual(game.runningScore, 4)

    def test_full_game1(self):
        game = g.Game("test")
        test_frames = [['6','3'], ['X'], ['5', '/'], ['6', '3'], ['X'],
                            ['X'], ['9', '/'], ['2', '0'], ['8', '/'],['X', 'X', 'X']]
        for x in test_frames:
            game.frame_input = x
            game.add_frame()
        self.assertEqual(game.runningScore,167)

    def test_full_game2(self):
        game = g.Game("test")
        test_frames = [['2', '7'], ['X'], ['X'], ['X'], ['7', '1'],
                            ['5', '/'], ['4', '/'], ['4', '1'], ['9', '0'], ['9', '/', '5']]
        for x in test_frames:
            game.frame_input = x
            game.add_frame()
        self.assertEqual(game.runningScore, 149)

    def test_full_game3(self):
        game = g.Game("test")
        test_frames = [['6', '2'], ['9', '/'], ['4', '4'], ['X'], ['X'],
                            ['9', '/'], ['6', '/'], ['3', '/'], ['8', '0'], ['3', '/', 'X']]
        for x in test_frames:
            game.frame_input = x
            game.add_frame()
        self.assertEqual(game.runningScore, 154)

    def test_full_game4(self):
        game = g.Game("test")
        test_frames = [['9', '0'], ['4', '4'], ['X'], ['5', '/'], ['7', '/'],
                            ['2', '2'], ['0', '0'], ['7', '2'], ['8', '1'], ['X', '1', '/']]
        for x in test_frames:
            game.frame_input = x
            game.add_frame()
        self.assertEqual(game.runningScore, 108)


    def test_full_game5(self):
        game = g.Game("test")
        test_frames = [['1', '1'], ['2', '2'], ['8', '/'], ['X'],
                            ['X'], ['X'], ['X'], ['8', '1'], ['5', '/'], ['1', '7']]
        for x in test_frames:
            game.frame_input = x
            game.add_frame()
        self.assertEqual(game.runningScore, 161)


if __name__ == '__main__':
    unittest.main()
