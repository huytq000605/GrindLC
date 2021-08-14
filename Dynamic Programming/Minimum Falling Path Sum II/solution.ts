function minFallingPathSum(grid: number[][]): number {
    let dp = Array(grid[0].length)
    for(let i = 0; i < grid[0].length; i++) {
        dp[i] = grid[0][i]
    }
    for(let row = 1; row < grid.length; row++) {
        let min = [Number.MAX_SAFE_INTEGER, -1]
        let secondMin = [Number.MAX_SAFE_INTEGER, -1]
        for(let i = 0; i < dp.length; i++) {
            if(dp[i] < min[0]) {
                secondMin = [...min]
                min = [dp[i], i]
            } else if(dp[i] < secondMin[0]) {
                secondMin = [dp[i], i]
            }
        }
        for(let col = 0; col < grid[0].length; col++) {
            if(col !== min[1]) {
                dp[col] = grid[row][col] + min[0]
            } else {
                dp[col] = grid[row][col] + secondMin[0]
            }
        }
    }
    return Math.min(...dp)
};