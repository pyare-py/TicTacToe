board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
valid = True
winner = None
current_player = "X"
next_player = "O"

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

def process(player):
    global winner
    global game_still_going
    global valid
    print(player + "'s turn.")
    for i in range(3, 0, -1):
        position = input("Choose a position from 1-9: ")
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = int(position) - 1
            if i - 1 > 0:
                print("\nWrong! Input\nNow You have only {} attemps\n".format(i - 1))
            else:
                game_still_going = False
                print("You can't attempt any more\n\nSo,", end=' ')
                valid = False
        elif board[int(position) - 1] != "-":
            if i - 1 > 0:
                print("\nYou can't go there. Go again.\nNow You have only {} attempt\n".format(i - 1))
            else:
                game_still_going = False
                print("You can't attempt any more\n\nSo,", end=' ')
                valid = False
        else:
            break
    if valid:
        board[int(position) - 1] = player
        display_board()

def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

while game_still_going:
    process(current_player)
    check_for_winner()
    if not valid:
        winner = next_player
    if "-" not in board:
        print("Tie")
        input()
    elif winner == "X" or winner == "O":
        print(winner + " won.")
        input()
    current_player, next_player = next_player, current_player