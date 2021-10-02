function calculateMinimumHP(dungeon: number[][]): number {
    let m = dungeon.length
    let n = dungeon[0].length
    let dp = Array(m).fill(0).map(() => Array(n))
    let dirs = [[0,1], [1,0]]
    let dfs = (i, j) => {
        if(dp[i][j] !== undefined) return dp[i][j]
        if(i === m - 1 && j === n - 1) {
            return Math.max(0, -dungeon[i][j])
        }
        let result = Math.max(Number.MAX_SAFE_INTEGER)
        for(let dir of dirs) {
            let row = i + dir[0]
            let col = j + dir[1]
            if(row >= m || col >= n) continue
            result = Math.min(result, Math.max(0, dfs(row, col) - dungeon[i][j]))
        }
        dp[i][j] = result
        return result
    }
    return dfs(0, 0) + 1
    
};