# Size of the grid
grid_size = 9

# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def print_grid(arr):
    for row in range(grid_size):
        for col in range(grid_size):
            print(str(arr[row][col]), end = ' ')
        print()

def check_exists_in_row(arr, row, num):
    if num in arr[row]:
        return True
    return False

def check_exists_in_col(arr, col, num):
    for row in arr:
        if row[col] == num:
            return True
    return False