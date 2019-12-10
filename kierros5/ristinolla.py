# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template

def print_board(board):
    x = 0
    j = 0
    for i in range(0,3):
        for j in range(0,3):
            print(board[j][i],end="")
        print()

def reorder_board(x,y,board,mark):
    if board[x][y] != ".":
        print("Error: a mark has already been placed on this square.")
        return -1
    board[x][y] = mark
    return board

def main():


    board = [[".",".","."], [".",".","."], [".",".","."]]
    print_board(board)

    # TODO: implement the datastructure for storing the board
    
    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            test = reorder_board(x,y,board,mark)
            if test == -1:
                continue
            else:
                board = test
                turns += 1
                print_board(board)
            # TODO: implement the turn of one player here


        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
