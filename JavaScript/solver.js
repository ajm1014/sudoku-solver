// 0 means unassigned cells
var board =  [[2, 0, 7, 0, 1, 0, 4, 0, 6],
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [3, 6, 0, 0, 0, 0, 0, 9, 1],
            [4, 0, 0, 6, 0, 5, 0, 0, 7],
            [0, 3, 0, 7, 2, 9, 0, 6, 0],
            [6, 0, 0, 1, 0, 4, 0, 0, 9],
            [1, 4, 0, 0, 0, 0, 0, 7, 3],
            [0, 0, 0, 0, 9, 0, 0, 0, 0],
            [9, 0, 6, 0, 4, 0, 1, 0, 8]];
            

// Prints the board to the console log
function printBoard(board) {
    let str = "\n";
    for (let rowIndex = 0; rowIndex < 9; rowIndex++) {
        for (let colIndex = 0; colIndex < 9; colIndex++) {
            str = str + board[rowIndex][colIndex] + " ";
        }
        str += "\n";
    }

    console.log(str);
}


// Returns the location of the next empty cell on the board
function findEmptyCell(board) {
    for (let rowIndex = 0; rowIndex < 9; rowIndex++) {
        for (let colIndex = 0; colIndex < 9; colIndex++) {
            if (board[rowIndex][colIndex] == 0) {
                return [rowIndex, colIndex];
            }
        }
    }

    // Return -1 if no empty cells are found
    return [-1, -1];
}


// Checks if the specified value can be entered into the specified cell on the board
function checkValue(board, row, col, value) {
    // Validate row is safe
    if (board[row].includes(value)) {
        return false;
    }

    // Validate column is safe
    for (let rowIndex = 0; rowIndex < board.length; rowIndex++) {
        if (board[rowIndex][col] == value) {
            return false;
        }
    }

    // Validate square is safe
    let squareRow = Math.floor(row / 3) * 3;
    let squareCol = Math.floor(col / 3) * 3;
    for (let rowOffset = 0; rowOffset < 3; rowOffset++) {
        for (let colOffset = 0; colOffset < 3; colOffset++) {
            if (board[squareRow + rowOffset][squareCol + colOffset] == value) {
                return false;
            }
        }
    }

    // Return true if the value passed all tests
    return true;
}


// Solve the board using a backtracking algorithm
function solveBoard(board) {
    let emptyCell = findEmptyCell(board);
    let row = emptyCell[0];
    let col = emptyCell[1];

    // If there are no empty cells, return
    if (row == -1) {
        return board;
    }

    // Try each safe value and recursively solve the board
    for (let value = 1; value <= 9; value++) {
        if (checkValue(board, row, col, value)) {
            board[row][col] = value;
            solveBoard(board);
        }
    }

    // If the board was not solvable from this position, backtrack and clear the cell
    if (findEmptyCell(board)[0] != -1) {
        board[row][col] = 0;
    }

    return board;
}


// Solve the board and print the results
if (solveBoard(board)) {
    printBoard(board);
}
else {
    solveBoard(board);
    console.log("This puzzle cannot be solved.");
}