# sets up initial empty grid
grid = {"7": " ", "8": " ", "9": " ",
        "4": " ", "5": " ", "6": " ",
        "1": " ", "2": " ", "3": " "}


def print_board():
    print("---------")
    print("| " + grid["7"] + " " + grid["8"] + " " + grid["9"] + " |")
    print("| " + grid["4"] + " " + grid["5"] + " " + grid["6"] + " |")
    print("| " + grid["1"] + " " + grid["2"] + " " + grid["3"] + " |")
    print("---------")


def make_move():
    marker = marker_switch()
    print("It is " + marker + "'s Turn.")
    grid_posistion = input("Enter grid posistion: ")
    VALID = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(grid_posistion) == 0:
        print("Please make an input.")
        make_move()
    elif len(grid_posistion) > 1 or grid_posistion not in VALID:
        print("Posistion should be from 1 to 9 and input as a numeral.")
        make_move()
    elif grid[grid_posistion] != " ":
        print("This cell is occupied! Choose another one!")
        make_move()
    else:
        grid[grid_posistion] = marker
        print_board()
        # make_move()
        game_state()


# checks the current state of the grid and re-calls make_move() until game ends
def game_state():
    play = ""

    for k, v in grid.items():
        play += v

    win_combos = [[grid["7"], grid["8"], grid["9"]],
                  [grid["4"], grid["5"], grid["6"]],
                  [grid["1"], grid["2"], grid["3"]],
                  [grid["7"], grid["4"], grid["1"]],
                  [grid["8"], grid["5"], grid["2"]],
                  [grid["9"], grid["6"], grid["3"]],
                  [grid["7"], grid["5"], grid["3"]],
                  [grid["1"], grid["5"], grid["9"]]]

    x_moves = play.count("X")
    o_moves = play.count("O")
    is_full_board = x_moves + o_moves == 9
    x_wins = len([c for c in win_combos if c.count("X") == 3])
    o_wins = len([c for c in win_combos if c.count("O") == 3])

    if x_wins and o_wins or max(x_moves, o_moves) - min(x_moves, o_moves) >= 2:
        print("Impossible")
    elif not x_wins and not o_wins and is_full_board:
        print("Game is a Draw!\n")
    elif x_wins:
        print("X wins, Congratulations! GG's!\n")
    elif o_wins:
        print("O wins, Congratulations! GG's!\n")
    else:
        make_move()


# used to change players marker on each turn using the current grid state
def marker_switch():
    marker = ""
    play = ""

    for k, v in grid.items():
        play += v

    x_moves = play.count("X")
    o_moves = play.count("O")

    if x_moves == 0:
        marker = "X"
    elif x_moves <= o_moves:
        marker = "X"
    else:
        marker = "O"

    return marker


def welcome():
    print("Welcome to my Tic-Tac-Toe game!\n")
    print("The rules are simple. 2 Players go head-to-head.")
    print("In a epic battle of cunning and strategy!")
    print("To be victorious! Match either three X's or O's in a horizontal,")
    print("vertical or diagonal line, before your opponent does.\n")
    print("The board is laid out as such:")
    print("---------")
    print("| 7 8 9 |")
    print("| 4 5 6 |")
    print("| 1 2 3 |")
    print("---------\n")
    print("Use your keyboard or the numpad to place your marker on that spot.")
    print("X is always the first marker placed.")
    print("Have fun! And may the best strategist win!\n")
    print("LET THE BATTLE BEGIN!")


# initiates the game
welcome()
print_board()
make_move()
