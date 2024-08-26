import random

def draw_board(board):
    print("------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-----------")

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            return row, col
        print("Invalid move! Try again.")

def get_computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    print("Welcome to Tic-Tac-Toe!")

    board = [[" " for _ in range(3)] for _ in range(3)]
    draw_board(board)

    players = ["X", "O"]
    random.shuffle(players)

    current_player = players[0]

    while True:
        if current_player == "X":
            row, col = get_player_move(board)
            board[row][col] = current_player
        else:
            print("Computer's turn:")
            row, col = get_computer_move(board)
            board[row][col] = current_player

        draw_board(board)

        if is_winner(board, current_player):
            print(f"{current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

play_game()
