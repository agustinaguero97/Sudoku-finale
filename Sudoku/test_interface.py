import unittest
import unittest.mock
from sudoku_interface import Interface


def boards(index):
    if index == 1:
        return [
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ]

    elif index == 2:
        return [
            [2, 3, 4, 1],
            [4, 1, 3, 2],
            [1, 4, 2, 3],
            [3, 2, 1, ""]
            ]

    elif index == 3:
        return [
            [5, 3, "", "", 7, "", "", "", ""],
            [6, "", "", 1, 9, 5, "", "", ""],
            ["", 9, 8, "", "", "", "", 6, ""],
            [8, "", "", "", 6, "", "", "", 3],
            [4, "", "", 8, "", 3, "", "", 1],
            [7, "", "", "", 2, "", "", "", 6],
            ["", 6, "", "", "", "", 2, 8, ""],
            ["", "", "", 4, 1, 9, "", "", 5],
            ["", "", "", "", 8, "", "", 7, 9]
        ]

    elif index == 4:
        return[
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, "", 7, 9]
            ]


class Test_interface(unittest.TestCase):

    @unittest.mock.patch("builtins.input", side_effect=["4"])
    def test_sudoku4_start(self, mock):
        game = Interface()
        game.set_game()
        self.assertEqual(game.size, 4)
        self.assertEqual(len(game.play.board[0]), 4)
        self.assertEqual(game.play.__class__.__name__, "Sudoku4")

    @unittest.mock.patch("builtins.input", side_effect=["9"])
    def test_sudoku9_start(self, mock):
        game = Interface()
        game.set_game()
        self.assertEqual(game.size, 9)
        self.assertEqual(len(game.play.board[0]), 9)
        self.assertEqual(game.play.__class__.__name__, "Sudoku9")

    @unittest.mock.patch("builtins.input", side_effect=["1", "2", "3"])
    def test_inputs(self, mock):
        game = Interface()
        game.user_inputs()
        self.assertEqual(game.number, "1")
        self.assertEqual(game.row, "2")
        self.assertEqual(game.column, "3")

    @unittest.mock.patch("builtins.input", side_effect=["4", "4", "4", "4"])
    def test_sudoku4_endgame(self, mock):
        game = Interface()
        game.set_game()
        game.play.set_board(boards(2))
        self.assertEqual(game.size, 4)
        self.assertEqual(len(game.play.board[0]), 4)
        self.assertTrue(game.play.is_playing)
        game.start_playing()
        self.assertFalse(game.play.is_playing)

    @unittest.mock.patch("builtins.input", side_effect=["9", "1", "9", "7"])
    def test_sudoku9_endgame(self, mock):
        game = Interface()
        game.set_game()
        game.play.set_board(boards(4))
        self.assertEqual(game.size, 9)
        self.assertEqual(len(game.play.board[0]), 9)
        self.assertTrue(game.play.is_playing)
        game.start_playing()
        self.assertFalse(game.play.is_playing)


if __name__ == '__main__':
    unittest.main()
