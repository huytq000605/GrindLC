function maximalSquare(matrix: string[][]): number {
    let dp = Array(matrix.length+1).fill(0).map(() => Array(matrix[0].length+1).fill(0))
    let result = 0
    for(let i = 1; i < dp.length; i++) {
        for(let j = 1; j < dp[0].length; j++) {
            if(matrix[i-1][j-1] === "1") {
                dp[i][j] = Math.min(dp[i - 1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                result = Math.max(result, dp[i][j])
            }
            
        }
    }
    return result*result // result is max edge
};