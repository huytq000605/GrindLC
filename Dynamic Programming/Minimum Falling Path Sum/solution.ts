function minFallingPathSum(matrix: number[][]): number {
    let dp = Array(matrix.length)
    for(let i = 0; i < matrix[0].length; i++) {
        dp[i] = matrix[0][i]
    }
    
    for(let row = 1; row < matrix.length; row++) {
        let prevCol = [...dp]
        for(let col = 0; col < matrix[0].length; col++) {
            let left = Number.MAX_SAFE_INTEGER
            let right = Number.MAX_SAFE_INTEGER
            let above = prevCol[col]
            if(col > 0) left = prevCol[col - 1]
            if(col < matrix[0].length - 1) right = prevCol[col + 1]
            dp[col] = Math.min(left, right, above) + matrix[row][col]
        }
    }
    
    return Math.min(...dp)
};