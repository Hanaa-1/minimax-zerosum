def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

def is_moves_left(board):
    return any(cell == '_' for row in board for cell in row)

def check_winner(board):
    # Check rows, columns, and diagonals
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

def minimax(board, depth, is_max):
    score = check_winner(board)
    if score is not None:
        return score

    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Main game loop
def main():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while check_winner(board) is None:
        # Player's turn
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == '_':
            board[row][col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        # Check if game is over
        if check_winner(board) is not None:
            break

        # AI's turn
        print("AI's turn:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)

    winner = check_winner(board)
    if winner == 1:
        print("AI wins!")
    elif winner == -1:
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()

