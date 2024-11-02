import java.util.Scanner;

public class TicTacToe {
    static char[][] board = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char currentPlayer = 'X';
        boolean gameOngoing = true;

        System.out.println("Welcome to Tic-Tac-Toe!");
        printBoard();

        while (gameOngoing) {
            System.out.println("Player " + currentPlayer + ", enter your move (row and column from 1 to 3): ");
            int row = scanner.nextInt() - 1;
            int col = scanner.nextInt() - 1;

            // Check if the chosen cell is valid
            if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
                board[row][col] = currentPlayer; // Place the player's symbol
                printBoard();

                // Check for a win or a draw
                if (checkWin(currentPlayer)) {
                    System.out.println("Player " + currentPlayer + " wins!");
                    gameOngoing = false;
                } else if (isBoardFull()) {
                    System.out.println("It's a draw!");
                    gameOngoing = false;
                } else {
                    // Switch player
                    currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
                }
            } else {
                System.out.println("Invalid move. Try again.");
            }
        }
        scanner.close();
    }

    // Print the current board
    public static void printBoard() {
        System.out.println("Current board:");
        for (int i = 0; i < 3; i++) {
            System.out.println(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2]);
            if (i < 2) System.out.println("---|---|---");
        }
    }

    // Check if the current player has won
    public static boolean checkWin(char player) {
        // Check rows, columns, and diagonals
        for (int i = 0; i < 3; i++) {
            if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) || // rows
                (board[0][i] == player && board[1][i] == player && board[2][i] == player)) { // columns
                return true;
            }
        }
        return (board[0][0] == player && board[1][1] == player && board[2][2] == player) || // main diagonal
               (board[0][2] == player && board[1][1] == player && board[2][0] == player);    // anti-diagonal
    }

    // Check if the board is full
    public static boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }
}
