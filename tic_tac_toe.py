""" Main document for the tic tac toe program. Imports the board class
    and uses it to construct a new board. """

from time import sleep
import board

new_board = board.Board()

player1 = True  # variable dictating whose turn it is


def player_move():
    """function governing a players turn"""
    global player1
    if player1:  # set player to X or O
        player = "X"
    else:
        player = "O"

    while True:
        moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # Ask for a square
        move = input(f"{player}, select your square: ")
        if move not in moves:  # check that the user entered a number 1-9
            print("Not a valid option, try again.")
            continue
        move = int(move)-1  # convert move to an integer
        if new_board.cells[move].status == "empty":  # verify the cell is empty
            new_board.cells[move].change_status(player)
            print("Legal Move")
            game_over = new_board.check_for_win()
            sleep(2)
            if player1:
                player1 = False
            else:
                player1 = True
            new_board.draw_board()
            if game_over:
                return False
            else:
                return True
        else:
            print("Not an open square. Try again.")


def main():
    """Main function. Sets up a new board and begins player turns until a winner emerges."""

    print("Welcome to Tic Tac Toe")
    sleep(1)
    new_board.draw_board()

    playing = True
    while playing:
        playing = player_move()
    print("Game Over")


if __name__ == "__main__":
    main()
