### template

def is_valid_state(state):
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
    # return
    
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)
        
def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions

# N-Queen
import sys
n = 4
# n = int(sys.stdin.readline())
    
def solveNQueens():
    solutions = []
    state = []
    search(state, solutions, n)
    print(solutions)

def is_valid_state(state, n):
    return len(state) == n

def get_candidates(state, n):
    if not state:
        return range(n)
    
    position = len(state)
    candidates = set(range(n))
            
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates

def search(state, solutions, n):
    if is_valid_state(state, n):
        state_string = state_to_string(state, n)
        solutions.append(state_string)
        return
    
    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()
        
def state_to_string(state, n):
    ret = []
    for i in state: 
        string = '.' * i + 'Q' + '.' * (n-i-1)
        ret.append(string)
    return ret

solveNQueens()

## solveSudoku (boj2580)
# input
# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0
# output
# 1 3 5 4 6 9 2 7 8
# 7 8 2 1 3 5 6 4 9
# 4 6 9 2 7 8 1 3 5
# 3 2 1 5 4 6 8 9 7
# 8 7 4 9 1 3 5 2 6
# 5 9 6 8 2 7 4 1 3
# 9 1 7 6 5 2 3 8 4
# 6 4 3 7 8 1 9 5 2
# 2 5 8 3 9 4 7 6 1

# when traversing the grid
from itertools import product
import sys

SHAPE = 9
GRID = 3
EMPTY = '0'
DIGITS = set([str(num) for num in range(1, SHAPE+1)])
board = []

for _ in range(SHAPE):
    board.append(sys.stdin.readline().split())

def solveSudoku():
    search(board)

def is_valid_state(board):
    for row in get_rows(board):
        if not set(row) == DIGITS:
            return False
        
    for col in get_cols(board):
        if not set(col) == DIGITS:
            return False
        
    for grid in get_grids(board):
        if not set(grid) == DIGITS:
            return False
        
    return True
        
def get_candidates(board, row, col):
    used_digits = set()
    used_digits.update(get_kth_row(board, row))
    used_digits.update(get_kth_col(board, col))
    used_digits.update(get_grid_at_row_col(board, row, col))
    used_digits -= set([EMPTY])
    candidates= DIGITS - used_digits
    return candidates

def search(board):
    if is_valid_state(board):
        return True
    
    for row_idx, row in enumerate(board):
        for col_idx, elm in enumerate(row):
            if elm == EMPTY:
                for candidate in get_candidates(board, row_idx, col_idx):
                    board[row_idx][col_idx] = candidate
                    
                    #recurse on the modified board
                    is_solved = search(board)
                    if is_solved:
                        return True
                    else:
                        #undo the wrong guess and start anew
                        board[row_idx][col_idx] == EMPTY
                        
                # exhausted all candidates but none solves the problem
                return False
    return True

# helper functions for retrieving rows, cols, and grids
def get_kth_row(board, k):
    return board[k]

def get_rows(board):
    for i in range(SHAPE):
        yield board[i]

def get_kth_col(board, k):
    return [
        board[row][k] for row in range(SHAPE)
    ]

def get_cols(board):
    for col in range(SHAPE):
        ret = [
                board[row][col] for row in range(SHAPE)
        ]
        yield ret

def get_grid_at_row_col(board, row, col):
    row = row // GRID * GRID
    col = col // GRID * GRID
    return [
        board[r][c] for r, c in 
        product(range(row, row + GRID), range(col, col + GRID))
    ]

def get_grids(board):
    for row in range(0, SHAPE, GRID):
        for col in range(0, SHAPE, GRID):
            grid = [
                board[r][c] for r, c in 
                product(range(row, row + GRID), range(col, col + GRID))
            ]
            yield grid
            
solveSudoku()

for i in range(SHAPE):
    line =' '.join(board[i])
    print(line)