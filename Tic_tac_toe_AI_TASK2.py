import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 6:
            print("-----------")
    print()


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]


def winner(board):
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def minimax(board, depth, alpha, beta, is_maximizing):
    win = winner(board)
    if win == AI:
        return 10 - depth   # prefer faster wins
    if win == HUMAN:
        return depth - 10   # prefer slower losses
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, alpha, beta, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # prune remaining branches
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, alpha, beta, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # prune remaining branches
        return best_score


def best_move(board):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice


def get_human_move(board):
    while True:
        try:
            choice = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue
        if choice not in range(9) or board[choice] != EMPTY:
            print("That spot isn't available. Try again.")
            continue
        return choice


def play():
    board = [EMPTY] * 9
    print("You are X. The AI is O. It plays perfectly, so the best you can do is tie!")
    print_board(board)

    current = HUMAN  # human goes first

    while True:
        if current == HUMAN:
            move = get_human_move(board)
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = best_move(board)
            board[move] = AI
            print(f"AI plays position {move + 1}")

        print_board(board)

        win = winner(board)
        if win:
            print(f"{win} wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        current = AI if current == HUMAN else HUMAN


if __name__ == "__main__":
play()
