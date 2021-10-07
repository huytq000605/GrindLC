function exist(board: string[][], word: string): boolean {
    let dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    let seen = Array(board.length).fill(0).map(() => Array(board[0].length).fill(false))
    let dfs = (i: number, j: number, idx: number) => {
        if(board[i][j] !== word[idx]) return false
        if(idx === word.length - 1) return true
        for(let dir of dirs) {
            let row = i + dir[0]
            let col = j + dir[1]
            if(row < 0 || row >= board.length || col < 0 || col >= board[0].length || seen[row][col]) continue
            seen[row][col] = true
            if(dfs(row, col, idx + 1)) return true
            seen[row][col] = false
        }
        return false
    }
    
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            if(board[i][j] === word[0]) {
                seen[i][j] = true
                if(dfs(i, j, 0)) return true
                seen[i][j] = false
            }
        }
    }
    return false
};