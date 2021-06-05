# Size of the grid
grid_size = 9

# 0 means unassigned cells
grid = [[2, 0, 7, 0, 1, 0, 4, 0, 6],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [3, 6, 0, 0, 0, 0, 0, 9, 1],
        [4, 0, 0, 6, 0, 5, 0, 0, 7],
        [0, 3, 0, 7, 2, 9, 0, 6, 0],
        [6, 0, 0, 1, 0, 4, 0, 0, 9],
        [1, 4, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [9, 0, 6, 0, 4, 0, 1, 0, 8]]


# Print the grid in the console window
def print_grid(arr):
    for row in range(grid_size):
        for col in range(grid_size):
            print(str(arr[row][col]), end = ' ')
        print()


# Find the next empty cell in the array
def get_next_blank(arr, cell):
    for row_num in range(grid_size):
        for col_num in range(grid_size):
            if arr[row_num][col_num] == 0:
                cell[0] = row_num
                cell[1] = col_num
                return True
    return False


# Check if a cell in the grid is safe to add a specific number
def is_safe(arr, row, col, num):
    # Check if the number already exists in the row
    if num in arr[row]:
        return False

    # Check if the number already exists in the column
    for single_row in arr:
        if single_row[col] == num:
            return False

    # Check if the number already exists in the box
    top_left = [(int(row / 3) * 3), (int(col / 3) * 3)]
    for row_num in range(top_left[0], (top_left[0] + 3)):
        for col_num in range(top_left[1], (top_left[1] + 3)):
            if arr[row_num][col_num] == num:
                return False

    # If it is safe, return true
    return True


# Recursively solve the puzzle using backtracking
def solve_puzzle(arr):
    cell = [0, 0]
    
    # Get the next empty cell, return if there are no empty cells remaining
    if not get_next_blank(arr, cell):
        return True

    # Fill the next empty cell with the next safe digit and recurse
    for num in range(1, 1 + grid_size):
        if is_safe(arr, cell[0], cell[1], num):
            arr[cell[0]][cell[1]] = num

            if solve_puzzle(arr):
                return True
            
            # If we were unable to complete the puzzle using that digit, backtrack the change and empty the cell
            arr[cell[0]][cell[1]] = 0

    # Return false if the puzzle cannot be solved from this point
    return False


# Solve the puzzle and print the result if possible
if solve_puzzle(grid):
    print_grid(grid)
else:
    print("This puzzle cannot be solved.")
