import unittest
from api import get_board_from_api


class Test_api(unittest.TestCase):

    def test_board_size_9(self):
        board = get_board_from_api(9)
        self.assertEqual(len(board), 9)
        for column in range(9):
            self.assertEqual(len(board[column]), 9)

    def test_board_size_4(self):
        board = get_board_from_api(4)
        self.assertEqual(len(board), 4)
        for column in range(4):
            self.assertEqual(len(board[column]), 4)

    def test_invalid_board_size(self):
        board = get_board_from_api(8)
        self.assertEqual(board, "invalid size")

    def test_invalid_board_size_string(self):
        board = get_board_from_api("nine")
        self.assertEqual(board, "invalid size")


if __name__ == '__main__':
    unittest.main()
