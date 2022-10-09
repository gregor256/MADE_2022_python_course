import unittest
from tictac import Player, TicTac


class PlayerTest(unittest.TestCase):
    def test_update(self):
        player = Player()
        player.update(0, 1)
        self.assertEqual(player.col, [0, 1, 0])
        self.assertEqual(player.row, [1, 0, 0])
        self.assertEqual(player.diagonal, 0)
        self.assertEqual(player.semi_diagonal, 0)

        player.update(0, 0)
        self.assertEqual(player.col, [1, 1, 0])
        self.assertEqual(player.row, [2, 0, 0])
        self.assertEqual(player.diagonal, 1)
        self.assertEqual(player.semi_diagonal, 0)

        player.update(2, 2)
        self.assertEqual(player.col, [1, 1, 1])
        self.assertEqual(player.row, [2, 0, 1])
        self.assertEqual(player.diagonal, 2)
        self.assertEqual(player.semi_diagonal, 0)

        player.update(2, 0)
        self.assertEqual(player.col, [2, 1, 1])
        self.assertEqual(player.row, [2, 0, 2])
        self.assertEqual(player.diagonal, 2)
        self.assertEqual(player.semi_diagonal, 1)

    def test_won(self):
        player = Player()
        player.update(0, 0)
        player.update(1, 1)
        player.update(2, 2)
        self.assertTrue(player.won())

        player = Player()
        player.update(2, 0)
        player.update(1, 1)
        player.update(0, 2)
        self.assertTrue(player.won())

        player = Player()
        player.update(1, 0)
        player.update(2, 0)
        player.update(0, 0)
        self.assertTrue(player.won())

        player = Player()
        player.update(1, 1)
        player.update(0, 1)
        player.update(2, 1)
        self.assertTrue(player.won())


class TicTacTest(unittest.TestCase):
    def test_analysis_result(self):
        game = TicTac()
        self.assertEqual(game.input_analysis('1 1'),
                         {'is_valid': True, 'content': (1, 1)})

        self.assertEqual(game.input_analysis('asdf'),
                         {'is_valid': False, 'message':
                             '2 coordinates expected. Try again.'})

        self.assertEqual(game.input_analysis(''),
                         {'is_valid': False, 'message':
                             '2 coordinates expected. Try again.'})

        self.assertEqual(game.input_analysis('1 2 3 '),
                         {'is_valid': False, 'message':
                             '2 coordinates expected. Try again.'})

        self.assertEqual(game.input_analysis('3 3'),
                         {'is_valid': False, 'message':
                             'Numbers between 0 and 2 expected. Try again.'})

        self.assertEqual(game.input_analysis('gg wp'),
                         {'is_valid': False, 'message':
                             'Digits expected. Try again.'})

    def test_game(self):
        game = TicTac(['1 1', '1 1'])
        game.start_game()
        self.assertEqual(game.last_sell_rewriting_attempt, '1 1')

        game = TicTac(['0 0', '0 1', '1 1', '0 2', '2 2'])
        self.assertEqual(game.start_game(), 'X won')

        game = TicTac(['1 0', '0 0', '0 1', '1 1', '0 2', '2 2'])
        self.assertEqual(game.start_game(), '0 won')

        game = TicTac(['0 0', '0 1', '0 2', '1 0', '1 1', '2 0',
                       '1 2', '2 2', '2 1'])
        self.assertEqual(game.start_game(), 'Draw')


if __name__ == '__main__':
    unittest.main()
