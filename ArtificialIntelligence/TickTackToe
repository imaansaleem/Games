import math
#defining constants
# Represents the empty cell on the Tic-Tac-Toe board
EMPTY = '-'
# Represents the human player
HUMAN = 'X'
# Represents the AI player
AI = 'O'
#Represents score of AI = 10
AIbenifit = 10
#Represents score of Human = -10
HumanBenifit = -10

def print_board(board):
    # Prints the current state of the board
    for row in board:
        print(' '.join(row))
    print()

def is_board_full(board):
    # Checks if the board is full
    for row in board:
        for cell in row:
            if cell==EMPTY:
                return False
    return True

def evaluate(board):
    # Evaluates the current state of the board
    # If the human player has won, it returns -10.
    # If the AI player has won, it returns 10.
    # If the game is a draw, it returns 0.
    # If the game is still ongoing, it returns 0.

    # Check rows who got all the three cells
    for row in board:
        # if count of all X is 3 human win
        if row.count(HUMAN) == 3:
            return HumanBenifit
        elif row.count(AI) == 3:
            return AIbenifit

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == HUMAN:
            return HumanBenifit
        elif board[0][col] == board[1][col] == board[2][col] == AI:
            return AIbenifit

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == HUMAN or board[0][2] == board[1][1] == board[2][0] == HUMAN:
        return HumanBenifit
    elif board[0][0] == board[1][1] == board[2][2] == AI or board[0][2] == board[1][1] == board[2][0] == AI:
        return AIbenifit

    return 0


def minimax(board, depth, alpha, beta, is_maximizing):
    # Minimax algorithm with alpha-beta pruning
    score = evaluate(board)

    if score != 0:
        return score

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI
                    best_score = max(best_score, minimax(board, depth + 1, alpha, beta, False))
                    board[row][col] = EMPTY
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    best_score = min(best_score, minimax(board, depth + 1, alpha, beta, True))
                    board[row][col] = EMPTY
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score


def find_best_move(board):
    # Finds the best move for the AI player using minimax algorithm
    best_score = float('-inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, 0, float('-inf'), float('inf'), False)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move


def play_game():
    # Plays a game of Tic-Tac-Toe

    #creating board
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(EMPTY)
        board.append(row)

    print("Tic-Tac-Toe - Human vs AI")
    print("Enter row and column numbers (0-2) to make a move.")
    print_board(board)

    while True:
        # Human's turn
        while True:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))

            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == EMPTY:
                board[row][col] = HUMAN
                break
            else:
                print("Invalid move. Try again.")

        print_board(board)

        if evaluate(board) == HumanBenifit:
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI is thinking...")
        row, col = find_best_move(board)
        board[row][col] = AI

        print_board(board)

        if evaluate(board) == AIbenifit:
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break


# Start the game
play_game()
