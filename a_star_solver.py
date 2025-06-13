from board_utils import copy_board, find_next_empty_cell, is_goal, is_valid
from heuristics import advanced_heuristic
import heapq
from board_gen import size

def solver_A_star(initial_board):
    board_set = [] 
    
    visited = set()

    g_score = 0
    h_score = advanced_heuristic(initial_board)
    f_score = g_score + h_score

    heapq.heappush(board_set, (f_score, g_score, initial_board))
    visited.add(tuple(map(tuple, initial_board)))

    while board_set:
        current_f, current_g, curr_board = heapq.heappop(board_set)

        if is_goal(curr_board):
            return curr_board

        empty_cell = find_next_empty_cell(curr_board)
        if empty_cell is None:
            continue
        row, col = empty_cell
    
        for number in range(1, size + 1):
            if is_valid(curr_board, empty_cell, number):
                new_board = copy_board(curr_board)
                new_board[row][col] = number

                board_tuple = tuple(map(tuple, new_board))
                
                if board_tuple in visited:
                    continue

                visited.add(board_tuple)

                new_g = current_g + 1 
                
                new_h = advanced_heuristic(new_board)
                
                new_f = new_g + new_h

                heapq.heappush(board_set, (new_f, new_g, new_board))

    return False 