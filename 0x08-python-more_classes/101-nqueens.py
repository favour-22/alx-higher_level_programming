#!/usr/bin/python3
import sys


def n_queens(N):
    """
    Solves the N-Queens problem for a chessboard of size N.
    Prints every possible solution to the problem, one solution per line.

    Parameters:
    N (int): the size of the chessboard and the number of queens to be placed on it

    Returns:
    None
    """
    def is_valid(board, row, col):
        """
        Checks whether it is safe to place a queen at the specified row and column on the board.

        Parameters:
        board (list): a list representing the chessboard
        row (int): the row to check
        col (int): the column to check

        Returns:
        bool: True if it is safe to place a queen at the specified row and column, False otherwise
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        """
        Recursively tries all possible configurations of queens on the board.

        Parameters:
        board (list): a list representing the chessboard
        row (int): the row to place a queen in

        Returns:
        None
        """
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    backtrack(board, 0)

    for sol in solutions:
        print(' '.join(str(col + 1) for col in sol))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    n_queens(N)
