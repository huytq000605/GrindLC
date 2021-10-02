function calculateMinimumHP(dungeon: number[][]): number {
    let m = dungeon.length
    let n = dungeon[0].length
    let dp = Array(m).fill(0).map(() => Array(n))
    dp[m - 1][n - 1] = Math.max(0, -dungeon[m - 1][n - 1])
    for(let i = m - 2; i >= 0; i--) {
        dp[i][n - 1] = Math.max(0, dp[i+1][n-1] - dungeon[i][n-1])
    }
    for(let i = n - 2; i >= 0; i--) {
        dp[m - 1][i] = Math.max(0, dp[m-1][i + 1] - dungeon[m-1][i])
    }
    for(let i = m - 2; i >= 0; i--) {
        for(let j = n - 2; j >= 0; j--) {
            dp[i][j] = Math.max(0, Math.min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        }
    }
    return dp[0][0] + 1
    
};