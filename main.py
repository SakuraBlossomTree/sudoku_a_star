from board_utils import print_board
# from solver import solver
from a_star_solver import solver_A_star as solver
from board_gen import puzzle_board, full_board
import time
from backtracking import backtrack

# board = [
#     [ 0, 3, 4, 0 ],
#     [ 4, 0, 0, 2 ],
#     [ 1, 0, 0, 3 ],
#     [ 0, 2, 1, 0 ],
# ]
board = puzzle_board
start = time.time()
print("Initial Board")
print_board(board)
print("------------------------")
print("Solved Board")
print_board(backtrack(board))
end = time.time()
print("Solved in:", end - start, "seconds")
print("\nSolution:")
for row in full_board:
    print(row)
