# sets up initial empty grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


# used as an easy call for when you need to render out the grid
def print_board():
    print("---------")
    print("| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |")
    print("| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |")
    print("| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |")
    print("---------")


# 1. allows player to make a move
# 2. move is allowed at the else statement in loop
# 3. adds marker to nested list variable - grid - and calls game_state()
def make_move():
    marker = marker_switch()
    coordinates = input("Enter the coordinates: ").split()
    VALID = ["1", "2", "3"]
    NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if coordinates[0] not in NUMBERS or coordinates[1] not in NUMBERS:
        print("You should enter numbers!")
        make_move()
    elif coordinates[0] not in VALID or coordinates[1] not in VALID:
        print("Coordinates should be from 1 to 3!")
        make_move()
    elif grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        make_move()
    else:
        grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = marker
        print_board()
        game_state()


# checks the current state of the grid and calls make_move() until game ends
def game_state():
    play = ""

    for item in grid:
        for character in item:
            play += character

    win_combos = [[grid[0][0], grid[0][1], grid[0][2]],
                  [grid[1][0], grid[1][1], grid[1][2]],
                  [grid[2][0], grid[2][1], grid[2][2]],
                  [grid[0][0], grid[1][0], grid[2][0]],
                  [grid[0][1], grid[1][1], grid[2][1]],
                  [grid[0][2], grid[1][2], grid[2][2]],
                  [grid[0][0], grid[1][1], grid[2][2]],
                  [grid[2][0], grid[1][1], grid[0][2]]]

    x_moves = play.count("X")
    o_moves = play.count("O")
    is_full_board = x_moves + o_moves == 9
    x_wins = len([c for c in win_combos if c.count("X") == 3])
    o_wins = len([c for c in win_combos if c.count("O") == 3])

    if x_wins and o_wins or max(x_moves, o_moves) - min(x_moves, o_moves) >= 2:
        print("Impossible")
    elif not x_wins and not o_wins and is_full_board:
        print("Draw")
    elif x_wins:
        print("X wins")
    elif o_wins:
        print("O wins")
    else:
        # print("Game not finished")
        make_move()


# used to change players marker on each turn using the current grid state
def marker_switch():
    marker = ""
    play = ""

    for item in grid:
        for character in item:
            play += character

    x_moves = play.count("X")
    o_moves = play.count("O")

    if x_moves == 0:
        marker = "X"
    elif x_moves <= o_moves:
        marker = "X"
    else:
        marker = "O"

    return marker


# initiates the game
print_board()
make_move()
