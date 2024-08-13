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
    found_solution = False
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(grid, row, column, number):
                        grid[row][column] = number
                        found_solution = solve(grid) or found_solution
                        grid[row][column] = 0
                return found_solution  # Return status to indicate if any solution was found
    print(np.matrix(grid))
    print()  # Print a blank line between solutions
    return True  # Return True when a solution is found

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
