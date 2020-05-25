board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_on = True
winner = None
current_turn = "x"


def display_board():
    print("|", board[0], "|", board[1], "|", board[2], "|", )
    print("|", board[3], "|", board[4], "|", board[5], "|", )
    print("|", board[6], "|", board[7], "|", board[8], "|", )


def turn():
    dis = input("press any number from 1 - 9")
    valid = False
    while not valid:
        while dis not in ["1", "2", "3",
                          "4", "5", "6",
                          "7", "8", "9", ]:
            dis = input("press any number from 1 - 9")

        position = int(dis) - 1

        if board[position] == "-":
            valid = True
        else:
            print("you cant go there")
        board[position] = current_turn

        display_board()


def play():
    display_board()

    while game_on:
        turn()
        game_over()
        flip_player()
    if winner == "x" or winner == "o":
        print(winner + " won!")

    elif winner == None:
        print("tie")


def game_over():
    win()
    tie()


def win():
    global winner
    row_winner = rows()
    column_winner = columns()
    diagonal_winner = diagonal()

    if row_winner:

        winner = row_winner


    elif column_winner:

        winner = column_winner


    elif diagonal_winner:

        winner = diagonal_winner


    else:
        winner = None


def rows():
    global game_on
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_on = False

    if row1:
        return board[0]

    elif row2:
        return board[3]


    elif row3:
        return board[6]

    else:
        return None


def columns():
    global game_on
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_on = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None


def diagonal():
    global winner
    global game_on
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[6] == board[4] == board[2] != "-"

    if dia1 or dia2:
        game_on = False

    if dia1:
        return board[0]
    elif dia2:
        return board[6]
    else:
        return None


def tie():
    global game_on
    if "-" not in board:
        game_on = False
        print("tie")
    else:
        return False


def flip_player():
    global current_turn
    if current_turn == "x":
        current_turn = "o"

    elif current_turn == "o":
        current_turn = "x"


play()
