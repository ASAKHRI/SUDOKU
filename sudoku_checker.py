import numpy as np

def verify(grid):

    lign = grid[:,0]
    colon = grid[0,:]
    case1 = grid[0:3, 0:3]
    case2 = grid[0:3, 3:6]
    case3 = grid[0:3, 6:9]
    case4 = grid[3:6, 0:3]
    case5 = grid[3:6, 3:6]
    case6 = grid[3:6, 6:9]
    case7 = grid[6:9, 0:3]
    case8 = grid[6:9, 3:6]
    case9 = grid[6:9, 6:9]
    val = 0

    for i in grid:

        if len(set(i)) != len(lign) and len(set(i)) != len(colon) and len(set(i)) != len(case1) and len(set(i)) != len(case2) and len(set(i)) != len(case3)and len(set(i)) != len(case4) and len(set(i)) != len(case5) and len(set(i)) != len(case6)and len(set(i)) != len(case7) and len(set(i)) != len(case8) and len(set(i)) != len(case9):
            val += 1
    if val == 0:
        return True
    else:
        return False
