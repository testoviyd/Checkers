import unittest
from backend.game_logic import CheckersBoard

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.board = CheckersBoard()

    def test_initial_setup(self):
        # Test initial board setup
        self.assertEqual(self.board.board[0][1], 'B')
        self.assertEqual(self.board.board[7][6], 'R')

    def test_valid_move(self):
        # Test a valid move
        self.board.move_piece(2, 1, 3, 0)
        self.assertEqual(self.board.board[3][0], 'B')
        self.assertEqual(self.board.board[2][1], '')

    def test_invalid_move(self):
        # Test an invalid move
        with self.assertRaises(ValueError):
            self.board.move_piece(0, 0, 1, 1)

if __name__ == '__main__':
    unittest.main()
