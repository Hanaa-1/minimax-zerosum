import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(3):
            print(f' {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ')
            if i < 2:
                print('---------')

    def is_valid_move(self, move):
        return self.board[move] == ' '

    def make_move(self, move):
        self.board[move] = self.current_player

    def check_winner(self):
        winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def minimax(self, depth=0, is_maximizing=True, alpha=-10000, beta=10000):
        if self.check_winner():
            if self.current_player == 'X':
                return 10 - depth
            else:
                return -10 + depth

        if is_maximizing:
            best_score = -10000
            for i in range(9):
                if self.board[i] == ' ':
                    self.make_move(i)
                    score = self.minimax(depth + 1, False, alpha, beta)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = 10000
            for i in range(9):
                if self.board[i] == ' ':
                    self.make_move(i)
                    score = self.minimax(depth + 1, True, alpha, beta)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return best_score

    def ai_move(self):
        best_score = -10000
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.make_move(i)
                score = self.minimax()
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.make_move(best_move)

def main():
    game = TicTacToe()
    print("Current state:")
    game.print_board()

    while True:
        # AI move
        ai_move = game.ai_move()
        print("AI move:")
        game.print_board()
        
        if game.check_winner():
            print("AI wins!")
            break
        
        # Human move
        human_move = input("Enter human move (0-8): ")
        if human_move.isdigit() and 0 <= int(human_move) < 9:
            human_move = int(human_move)
            game.make_move(human_move)
            print("Human move:")
            game.print_board()
            
            if game.check_winner():
                print("Human wins!")
                break
        else:
            print("Invalid input. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    main()