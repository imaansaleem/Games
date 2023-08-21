## Tic-Tac-Toe using Minimax Algorithm

This repository contains a simple implementation of the Tic-Tac-Toe game with an AI player using the Minimax algorithm. The AI player is capable of making optimal moves by evaluating possible moves and outcomes using the Minimax algorithm with alpha-beta pruning.

### How the Code Works

The implementation is divided into several functions, each serving a specific purpose:

- **print_board(board):** Prints the current state of the Tic-Tac-Toe board.

- **is_board_full(board):** Checks if the board is full (no more available moves).

- **evaluate(board):** Evaluates the current state of the board. If the human player (X) has won, it returns -10. If the AI player (O) has won, it returns 10. If the game is a draw, it returns 0.

- **minimax(board, depth, alpha, beta, is_maximizing):** Implements the Minimax algorithm with alpha-beta pruning. This function recursively evaluates possible moves and outcomes to find the best move for the AI player. It returns the score associated with each move.

- **find_best_move(board):** Finds the best move for the AI player by calling the `minimax` function for each available move and selecting the move with the highest score.

- **play_game():** Initiates the game loop, allowing the human player to make moves and playing against the AI player. The AI uses the `find_best_move` function to make its moves.

### How to Play

1. Follow the prompts to make your moves by entering row and column numbers (0-2).
2. The AI player will automatically respond with its moves.
3. The game will display the winner (if any) or indicate a draw when the game is over.
