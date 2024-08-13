import numpy as np

def possible(grid, row, column, number):
    for i in range(9):
        if grid[row][i] == number:
            return False
    for i in range(9):
        if grid[i][column] == number:
            return False
    x = (column // 3) * 3
    y = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y + i][x + j] == number:
                return False
    return True

def solve(grid):
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(grid, row, column, number):
                        grid[row][column] = number
                        if solve(grid):
                            return True
                        grid[row][column] = 0
                return False  # Return False if no number can be placed
    print(np.matrix(grid))
    return True

grid = [[9,0,6,0,7,0,4,0,3],
        [0,0,0,4,0,0,2,0,0],
        [0,7,0,0,2,3,0,1,0],
        [5,0,0,0,0,0,1,0,0],
        [0,4,0,2,0,8,0,6,0],
        [0,0,3,0,0,0,0,0,5],
        [0,3,0,7,0,0,0,5,0],
        [0,0,7,0,0,5,0,0,0],
        [4,0,5,0,1,0,7,0,8]]

if not solve(grid):
    print("No solution exists.")
