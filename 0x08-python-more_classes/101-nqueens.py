#!/usr/bin/python3
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    """Create a deep copy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Retrieve the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """Mark spots on a chessboard as non-attackable."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    for r, c in zip(range(row + 1, len(board)), range(col + 1, len(board))):
        if c >= len(board):
            break
        board[r][c] = "x"
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if c < 0:
            break
        board[r][c] = "x"
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if c >= len(board):
            break
        board[r][c] = "x"
    for r, c in zip(range(row + 1, len(board)), range(col - 1, -1, -1)):
        if c < 0:
            break
        board[r][c] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
