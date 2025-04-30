def solve_n_queens(n):
    def print_solution(board):
        for row in board:
            print(" ".join("Q" if col else "." for col in row))
        print("\n" + "-" * (2 * n - 1))

    def is_safe(row, col):
        return not cols[col] and not diag1[row - col] and not diag2[row + col]

    def place_queen(row):
        if row == n:
            print_solution(board)
            solutions.append([row.index(1) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                cols[col] = diag1[row - col] = diag2[row + col] = True

                place_queen(row + 1)

                # Backtrack
                board[row][col] = 0
                cols[col] = diag1[row - col] = diag2[row + col] = False

    # Initialize board and constraints
    board = [[0 for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diag1 = {}
    diag2 = {}
    for i in range(-n + 1, n): diag1[i] = False
    for i in range(2 * n): diag2[i] = False

    solutions = []
    place_queen(0)
    return solutions

# Example usage
n = 8
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
