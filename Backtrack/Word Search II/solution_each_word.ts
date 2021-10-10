function findWords(board: string[][], words: string[]): string[] {
    let startWith = new Map()
    for(let word of words) {
        if(!startWith.has(word[0])) startWith.set(word[0], new Set())
        startWith.get(word[0]).add(word)
    }
    let result = []
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            let letter = board[i][j]
            if(startWith.has(letter)) {
                let deleted = []
                let wordSet = startWith.get(letter)
                for(let word of wordSet.values()) {
                    if(findWord(board, i, j, word)) {
                        result.push(word)
                        deleted.push(word)
                    }
                    for(let del of deleted) {
                        wordSet.delete(del)
                    }
                }
            }
        }
    }
    return result
};

function findWord(board: string[][], i: number, j: number, word: string): boolean {
    let dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
    let seen = Array(board.length).fill(0).map(() => Array(board[0].length))
    let dfs = (i: number, j: number, idx: number) => {
        if(idx >= word.length) return true
        seen[i][j] = true
        for(let dir of dirs) {
            let row = i + dir[0]
            let col = j + dir[1]
            if(row < 0 || col < 0 || row >= board.length || col >= board[0].length || board[row][col] !== word[idx] || seen[row][col]) continue
            if(dfs(row, col, idx + 1)) return true
        }
        seen[i][j] = false
        return false
    }
    if(dfs(i, j, 1)) return true
    return false
    
}