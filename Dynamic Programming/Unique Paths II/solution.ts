function uniquePathsWithObstacles(grid: number[][]): number {
    if(grid[0][0] === 1) return 0
    let dp = Array(grid.length + 1).fill(0).map(() => Array(grid[0].length + 1).fill(0))
    dp[1][1] = 1
    
    for(let i = 1; i < dp.length; i++) {
        for(let j = 1; j < dp[0].length; j++) {
            if(grid[i - 1][j - 1] === 0) dp[i][j] += dp[i - 1][j] + dp[i][j-1]
        }
    }
    return dp[dp.length - 1][dp[0].length - 1]
    
};