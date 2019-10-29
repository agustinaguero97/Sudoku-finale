from sudoku import Sudoku4, Sudoku9
from api import get_board_from_api


class Interface():

    def __init__(self):
        self.size = 9
        self.play = ""
        self.number = ""
        self.row = ""
        self.column = ""

    def get_size(self):
        size = ""
        while size not in ('4', '9'):
            size = input("what size do you want the board to be? Answer '4' or '9'\n").lower()
            if size not in('4', '9'):
                print("Please answer with '4' or '9'\n")
            if size == "9":
                self.size = 9
                self.play = Sudoku9()
            elif size == "4":
                self.size = 4
                self.play = Sudoku4()

    def set_game(self):
        self.get_size()
        self.play.set_board(get_board_from_api(self.size))

    def start_playing(self):
        print("game starto!")
        while self.play.is_playing:
            print(self.play.board_print())
            self.user_inputs()
            self.play.play(self.number, self.row, self.column)
            if self.play.error != "":
                print("\nError\n" + self.play.error)
        print(self.play.board_print())
        print("congrats! youve won")

    def user_inputs(self):
        self.number = input("what number do you want to place\n(from 0 to 9)? ")
        self.row = input("what row? ")
        self.column = input("what column? ")


game = Interface()
game.set_game()
game.start_playing()

""" esto para abajo es viejo

def main():
    number = 0
    row = 0
    column = 0
    selection = 0
    static = 0
    while selection != "4" and selection != "9":
        selection = input("what version do you wanna play? input 4 or 9:")
    while static != "y" and static != "n":
        static = input("do you wanna play with a static board?:")
    if selection == "9":
        print ("starting game")
        print ("rows and colums go from 1 to 9, not from 0 to 8")
        game = Sudoku_9()
        if static == "y":
            game.set_board([
                [5, 3, "", "", 7, "", "", "", ""],
                [6, "", "", 1, 9, 5, "", "", ""],
                ["", 9, 8, "", "", "", "", 6, ""],
                [8, "", "", "", 6, "", "", "", 3],
                [4, "", "", 8, "", 3, "", "", 1],
                [7, "", "", "", 2, "", "", "", 6],
                ["", 6, "", "", "", "", 2, 8, ""],
                ["", "", "", 4, 1, 9, "", "", 5],
                ["", "", "", "", 8, "", "", 7, 9]
            ])

        elif static == "n":
            game.set_board(get_board_from_api(9))
        while game.is_playing:
            game.board_print()
            number = input("wich number do you want to place?: ")
            row= input("wich ROW: ")
            column = input("wich COLUMN:")
            game.play(number,row, column)

        print("victory")

    elif selection == "4":
        print("starting game")
        print("rows and column go from 1 to 4, not from 0 to 3")
        game = Sudoku_4()
        if static == "y":
            game.set_board ([
                ["", 3, 4, ""],
                [4, "", "", 2],
                [1, "", "", 3],
                ["", 2, 1, ""]
            ])
        elif static == "n":
            game.set_board(get_board_from_api(4))
        while game.is_playing:
            game.board_print()
            number = input("wich number do you want to place?:")
            row = input("wich ROW: ")
            column = input("wich COLUMN: ")
            game.play(number,row, column)
        print("victory")

main()
"""
