#!/usr/bin/python3


import sys

def is_safe(board, row, col, N):
    """
    Check if placing a queen at [row, col] is safe in the current configuration of the board.

    Args:
    - board (list): The current board configuration.
    - row (int): Row index to check.
    - col (int): Column index to check.
    - N (int): Size of the board.

    Returns:
    - bool: True if placing a queen is safe, False otherwise.
    """
    # Check if there is a queen in the current row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve(board, col, N):
    """
    Recursively solve the N-Queens problem using backtracking.

    Args:
    - board (list): The current board configuration.
    - col (int): Current column index.
    - N (int): Size of the board.

    Returns:
    - bool: True if a solution is found, False otherwise.
    """
    if col >= N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve(board, col + 1, N) or res
            board[i][col] = 0

    return res

def print_solution(board, N):
    """
    Print a single solution of the N-Queens problem.

    Args:
    - board (list): The current board configuration.
    - N (int): Size of the board.
    """
    sol = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sol.append([i, j])
    print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
