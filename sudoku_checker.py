import numpy as np

def checker(sudoku):

    grid = np.asarray(sudoku)

    def row(grid):
        row = grid[i,:]
        return len(set(row)) == len(row)

    def column(grid):
        column = grid[:,i]
        return len(set(column)) == len(column)

    def case(grid):
        case = grid.reshape(3, 3,-1, 3).swapaxes(1,2).reshape(-1, 3, 3)
        for i in range (3):
            if not row(grid):
                return False
            if not column(grid):
                return False
            else:
                return True

    for i in range (9):
        if not row(grid):
            return False
        if not column(grid):
            return False
        if not case(grid):
            return False
        else:
            return True
