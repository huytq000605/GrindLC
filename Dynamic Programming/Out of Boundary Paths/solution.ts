function findPaths(m: number, n: number, maxMove: number, startRow: number, startColumn: number): number {
    let dirs = [[0,1], [1,0], [-1,0], [0, -1]]
    let cache = Array(m).fill(0).map(() => Array(n).fill(0).map(() => Array(maxMove)))
    let MOD = 1e9 + 7
    let dfs = (row: number, col: number, move: number) => {
        let result = 0
        if(cache[row][col][move] !== undefined) return cache[row][col][move]
        if(move > 0) {
            for(let dir of dirs) {
                let newRow = row + dir[0]
                let newCol = col + dir[1]
                if(newRow < 0 || newRow >= m || newCol < 0 || newCol >= n) {
                    result++
                } else {
                    result += dfs(newRow, newCol, move - 1)
                    result = result % MOD
                }
            }
        }
        cache[row][col][move] = result
        return result
    }
    
    return dfs(startRow, startColumn, maxMove) % MOD
};