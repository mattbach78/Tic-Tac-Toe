"""Module creating the Board class, modeling a new Tic Tac Toe board."""

from squares import Square


class Board():

    """ Class to define a board, draw it to the terminal, and check for a winner"""

    def __init__(self):
        """Initializes a list of cells and calls the set_board method"""
        self.cells = []
        self.set_board()

    def set_board(self):
        """Creates new square objects for each cell and appends them to the self.cells list"""
        for i in range(0, 9):
            square = Square(i)
            self.cells.append(square)

    def draw_board(self):
        """Code used to redraw the board after a change is made."""
        for box in self.cells:
            if box.status == "empty":
                box.to_print = box.location+1
            else:
                box.to_print = box.status
        print("Here is the current board:\n")
        print(
            f" {self.cells[0].to_print} | {self.cells[1].to_print} | {self.cells[2].to_print} ")
        print("---|---|---")
        print(
            f" {self.cells[3].to_print} | {self.cells[4].to_print} | {self.cells[5].to_print} ")
        print("---|---|---")
        print(
            f" {self.cells[6].to_print} | {self.cells[7].to_print} | {self.cells[8].to_print} \n")

    def change_cell(self, cell_num, marker):
        """Code that sets a given cell (based on cell_num) to a given value (marker)"""
        self.cells[cell_num] = marker

    # code to check for a winner. Returns True if winner found.
    def check_for_win(self):
        """If tree to evaluate a winner. Returns True if a winner is found."""
        if self.cells[0].status == self.cells[1].status and self.cells[1].status == \
                self.cells[2].status and self.cells[0].status != "empty":
            print(f"{self.cells[0].status} wins on the top row!")
        elif self.cells[3].status == self.cells[4].status and self.cells[4].status == \
                self.cells[5].status and self.cells[3].status != "empty":
            print(f"{self.cells[3].status} wins on the middle row!")
        elif self.cells[6].status == self.cells[7].status and self.cells[7].status == \
                self.cells[8].status and self.cells[6].status != "empty":
            print(f"{self.cells[6].status} wins on the bottom row!")
        elif self.cells[0].status == self.cells[3].status and self.cells[3].status == \
                self.cells[6].status and self.cells[0].status != "empty":
            print(f"{self.cells[0].status} wins on the left column!")
        elif self.cells[1].status == self.cells[4].status and self.cells[4].status == \
                self.cells[7].status and self.cells[1].status != "empty":
            print(f"{self.cells[1].status} wins on the middle column!")
        elif self.cells[2].status == self.cells[5].status and self.cells[5].status == \
                self.cells[8].status and self.cells[2].status != "empty":
            print(f"{self.cells[2].status} wins on the right column!")
        elif self.cells[0].status == self.cells[4].status and self.cells[4].status == \
                self.cells[8].status and self.cells[0].status != "empty":
            print(f"{self.cells[0].status} wins on the diagonal down!")
        elif self.cells[6].status == self.cells[4].status and self.cells[4].status == \
                self.cells[2].status and self.cells[6].status != "empty":
            print(f"{self.cells[6].status} wins on the diagonal up!")
        else:
            print("No winner yet, next player.")
            return False
        return True
