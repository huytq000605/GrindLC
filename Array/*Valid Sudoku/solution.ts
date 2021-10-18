function isValidSudoku(board: string[][]): boolean {
    let n = board.length
    let rowSet = Array(n)
    let colSet = Array(n)
    let squareSet = Array(n)
    for(let i = 0; i < n; i++) {
        rowSet[i] = new Set()
        colSet[i] = new Set()
        squareSet[i] = new Set()
    }
    for(let row = 0; row < n; row++) {
        for(let col = 0; col < n; col++) {
            if(board[row][col] !== ".") {
                let val = Number(board[row][col])
                let squareIdx = Math.floor(row / 3) * 3 + Math.floor(col / 3)
                if(rowSet[row].has(val) || colSet[col].has(val) || squareSet[squareIdx].has(val)) return false
                rowSet[row].add(val)
                colSet[col].add(val)
                squareSet[squareIdx].add(val)
            }
            
            
        }
    }
    return true
};