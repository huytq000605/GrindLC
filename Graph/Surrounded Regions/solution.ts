/**
 Do not return anything, modify board in-place instead.
 */
 function solve(board: string[][]): void {
    const dirs = [[0,1], [1,0], [-1,0], [0, -1]]
    let dfs = (i, j) => {
        board[i][j] = "."
        for(let dir of dirs) {
            let row = i + dir[0]
            let col = j + dir[1]
            if(row < 0 || col < 0 || row >= board.length || col >= board[0].length || board[row][col] === "." || board[row][col] === "X") continue
            dfs(row, col)
        }
    }
    for(let col = 0; col < board[0].length; col++) {
        if(board[0][col] === "O") {
            dfs(0, col)
        }
        if(board.length - 1 !== 0 && board[board.length - 1][col] === "O") {
            dfs(board.length - 1, col)
        }
    }
    
    for(let row = 0; row < board.length; row++) {
        if(board[row][0] === "O") {
            dfs(row, 0)
        }
        if(board[0].length - 1 !== 0 && board[row][board[0].length - 1] === "O") {
            dfs(row, board[0].length - 1)
        }
    }

    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            if(board[i][j] === ".") board[i][j] = "O"
            else board[i][j] = "X"
        }
    }
};