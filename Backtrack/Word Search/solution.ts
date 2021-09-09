function exist(board: string[][], word: string): boolean {
    let dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    let dfs = (i, j, idx) => {
        if(idx === word.length) return true
        seen[i][j] = true
        for(let dir of dirs) {
            let newRow = i + dir[0]
            let newCol = j + dir[1]
            if(newRow < 0 || newCol < 0 || newRow >= board.length || newCol >= board[0].length || board[newRow][newCol] !== word[idx] || seen[newRow][newCol]) continue
            if(dfs(newRow, newCol, idx+1)) return true
        }
        seen[i][j] = false
        return false
    }
    
    let seen = Array(board.length).fill(0).map(() => Array(board[0].length))
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            if(board[i][j] === word[0]) {
                if(dfs(i, j, 1)) return true
            }
        }
    }
    
    return false
};