from board_utils import copy_board, find_next_empty_cell, is_goal, is_valid
from heuristics import count_empty_cells, advanced_heuristic
import heapq
from board_gen import size

n = size+1

def count_filled_cells(board):
    count = 0
    for row in board:
        for cell in row:
            if cell != 0:
                count+=1
    return count

def solver(initial_board):
    board_set = [] 
    f = 0
    heapq.heappush(board_set, (f, initial_board))
    while board_set:
        _, curr_board = heapq.heappop(board_set)

        if is_goal(curr_board):
            return curr_board

        empty_cell = find_next_empty_cell(curr_board)
        row, col = empty_cell
    
        if empty_cell is None:
            continue

        for number in range(n):
            if is_valid(curr_board, empty_cell, number):
                new_board = copy_board(curr_board)
                new_board[row][col] = number

                g = count_filled_cells(new_board) 
                h = count_empty_cells(new_board)
                f = g + h

                heapq.heappush(board_set, (f, new_board))

    return False 