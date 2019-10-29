import unittest
from sudoku import Sudoku_4

class Test_Sudoku_4(unittest.TestCase):

    def test_board_set(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        print(game.board)
        print(game.original_numbers)
        self.assertTrue(game.is_playing)

    def test_valid_number(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,4)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board, [
            ["", 3, 4, 1],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        self.assertFalse(game.error)
    
    def test_wrong_number(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,1)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            [1, 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_replace_number(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,1)
        self.assertEqual(game.board,[
            [1, 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(2,1,1)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            [2, 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_replacement(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,2)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])

    def test_victory(self):
        game = Sudoku_4()
        game.set_board([
            [2, 3, 4, 1],
            [4, 1, 3, 2],
            [1, 4, 2, 3],
            [3, 2, 1, ""]
        ])
        game.play(4,4,4)
        self.assertFalse(game.is_playing)
        self.assertEqual(game.board,[
            [2, 3, 4, 1],
            [4, 1, 3, 2],
            [1, 4, 2, 3],
            [3, 2, 1, 4]
        ])

    def test_no_victory(self):
        game = Sudoku_4()
        game.set_board([
            [2, 3, 4, 1],
            [4, 1, 3, 2],
            [1, 4, 2, 3],
            [3, 2, 1, ""]
        ])
        game.play(1,4,4)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            [1, 2, 3, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2],
            [2, 3, 4, 1]
        ])
    
    def test_invalid_number_string(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play("from",1,1)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_number_big(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(15,1,1)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_number_small(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(0,1,1)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_row_string(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,"grom",3)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_row_big(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,11,3)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_row_small(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,-4,3)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_column_string(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,"rolando")
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_column_big(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,40)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
    
    def test_invalid_column_small(self):
        game = Sudoku_4()
        game.set_board([
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])
        game.play(1,1,0)
        self.assertTrue(game.is_playing)
        self.assertEqual(game.board,[
            ["", 3, 4, ""],
            [4, "", "", 2],
            [1, "", "", 3],
            ["", 2, 1, ""]
        ])

if __name__=='__main__':
    unittest.main()