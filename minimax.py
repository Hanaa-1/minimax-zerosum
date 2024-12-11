import tkinter as tk
from tkinter import messagebox

# Functions for Minimax AI with Alpha-Beta Pruning and Heuristic Evaluation
def is_moves_left(board):
    return any(cell == '_' for row in board for cell in row)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return 1 if row[0] == 'O' else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return 1 if board[0][col] == 'O' else -1
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 1 if board[0][0] == 'O' else -1
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 1 if board[0][2] == 'O' else -1
    return 0 if not is_moves_left(board) else None
                    current_score = minimax(board, depth + 1, not is_max, alpha, beta)
                    best = max(best, current_score)
                    print(f"Depth {depth}: Evaluating move (O) at ({i}, {j}) with score {current_score}")
                    board[i][j] = '_'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    current_score = minimax(board, depth + 1, not is_max, alpha, beta)
                    best = min(best, current_score)
                    print(f"Depth {depth}: Evaluating move (X) at ({i}, {j}) with score {current_score}")
                    board[i][j] = '_'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, -float('inf'), float('inf'))
                print(f"Evaluating best move at ({i}, {j}) with score {move_val}")
                board[i][j] = '_'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# GUI Class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root, text='', font=('Arial', 24), height=2, width=5,
                    command=lambda i=i, j=j: self.player_move(i, j)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def player_move(self, i, j):
        if self.board[i][j] == '_':
            self.board[i][j] = 'X'
            self.buttons[i][j].config(text='X', state=tk.DISABLED)
            winner = check_winner(self.board)
            if winner is not None:
                self.end_game(winner)
                return
            self.ai_move()
        else:
            messagebox.showwarning("Invalid Move", "This cell is already taken!")

    def ai_move(self):
        ai_move = find_best_move(self.board)
        if ai_move != (-1, -1):
            self.board[ai_move[0]][ai_move[1]] = 'O'
            self.buttons[ai_move[0]][ai_move[1]].config(text='O', state=tk.DISABLED)
        winner = check_winner(self.board)
        if winner is not None:
            self.end_game(winner)

    def end_game(self, winner):
        if winner == 1:
            messagebox.showinfo("Game Over", "AI wins!")
        elif winner == -1:
            messagebox.showinfo("Game Over", "You win!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()

    def reset_game(self):
        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
