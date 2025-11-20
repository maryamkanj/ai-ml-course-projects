import tkinter
from tkinter import messagebox  # for User Interface

# XO grid (3x3)
board = [" " for i in range(9)]
current_player = "X"  # the human starts first


# function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


# function to check if the board is full
def is_board_full(board):
    return " " not in board


def minimax(board, is_maximizing):
    if check_winner(board, "X"):  # Fixed: was "winner"
        return -1
    elif check_winner(board, "O"):
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:  # ai move
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # ai makes a move
                score = minimax(board, False)  # switch to minimizing player
                board[i] = " "  # undo the move
                best_score = max(best_score, score)
        return best_score
    else:  # human's move
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # human makes a move
                score = minimax(board, True)  # switch to maximizing player
                board[i] = " "  # undo the move
                best_score = min(best_score, score)  # Fixed: should be min for minimizing player
        return best_score


def best_move():
    best_move_index = None  # Fixed: renamed variable to avoid conflict
    best_score = -float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # ai makes a move
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move_index = i
    return best_move_index  # Fixed: need to return the best move


def player_move(index):  # Fixed: added index parameter
    global current_player
    if board[index] == " " and current_player == "X":
        board[index] = "X"
        buttons[index].config(text="X")  # Fixed: was 'button' should be 'buttons'
        if check_winner(board, "X"):
            messagebox.showinfo("tic-tac-toe", "you win !!")
            reset_board()
        elif is_board_full(board):
            messagebox.showinfo("tic-tac-toe", "its a draw !!")
            reset_board()
        else:
            current_player = "O"  # no winner switch turns to ai
            ai_move()


def ai_move():
    global current_player
    index = best_move()
    if index is not None:  # Added safety check
        board[index] = 'O'
        buttons[index].config(text="O")  # Fixed: was 'button' should be 'buttons'
        if check_winner(board, "O"):
            messagebox.showinfo("tic-tac-toe", "ai wins !!")
            reset_board()
        elif is_board_full(board):
            messagebox.showinfo("tic-tac-toe", "its a draw !!")
            reset_board()
        else:
            current_player = "X"  # no winner switch turns to human


def reset_board():
    global board, current_player
    board = [" " for i in range(9)]  # Fixed: reset the board array
    current_player = "X"  # human starts the game
    for button in buttons:
        button.config(text=" ")


root = tkinter.Tk()
root.title("tic-tac-toe")
buttons = []
for i in range(9):
    button = tkinter.Button(root,
                            text=" ",
                            font=("normal", 40, "normal"),
                            width=5,
                            height=2,
                            command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()