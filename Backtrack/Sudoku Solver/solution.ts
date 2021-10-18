/**
 Do not return anything, modify board in-place instead.
 */
 function solveSudoku(board: string[][]): void {
    let rowSet = Array(board.length)
    let colSet = Array(board.length)
    let squareSet = Array(board.length)
    for(let i = 0; i < board.length; i++) {
        rowSet[i] = new Set()
        colSet[i] = new Set()
        squareSet[i] = new Set()
    }

    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board.length; j++) {
            if(board[i][j] !== ".") {
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                let squareIdx = Math.floor(i / 3) * 3 + Math.floor(j / 3)
                squareSet[squareIdx].add(board[i][j])
            }
        }
    }

    let isValid = (row, col, value) => {
        if(rowSet[row].has(value)) return false
        if(colSet[col].has(value)) return false
        let squareIdx = Math.floor(row / 3) * 3 + Math.floor(col / 3)
        if(squareSet[squareIdx].has(value)) return false
        return true
    }
    
    let add = (row, col, value) => {
        rowSet[row].add(value)
        colSet[col].add(value)
        let squareIdx = Math.floor(row / 3) * 3 + Math.floor(col / 3)
        squareSet[squareIdx].add(value)
        board[row][col] = value
    }
    
    let remove = (row, col, value) => {
        rowSet[row].delete(value)
        colSet[col].delete(value)
        let squareIdx = Math.floor(row / 3) * 3 + Math.floor(col / 3)
        squareSet[squareIdx].delete(value)
        board[row][col] = "."
    }
    
    

    let dfs = () => {
        for(let i = 0; i < board.length; i++) {
            for(let j = 0; j < board[0].length; j++) {
                if(board[i][j] === ".") {
                    for(let n = 1; n < 10; n++) {
                        let c = String(n)
                        if(isValid(i, j, c)) {
                            add(i, j, c)
                            if(dfs()) return true
                            remove(i, j, c)
                        }
                        
                    }
                    return false
                }
            }
        }
        return true
    }
    
    dfs()
};