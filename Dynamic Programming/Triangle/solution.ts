function minimumTotal(triangle: number[][]): number {
    let dp = Array(triangle.length).fill(0).map((_, index) => Array(index + 1).fill(0))
    dp[0][0] = triangle[0][0]
    let row = 1
    while(row < dp.length) {
        for(let i = 0; i < dp[row].length; i++) {
            let left
            let right
            if(i - 1 < 0 || i - 1 >= dp[row - 1].length) left = Number.MAX_SAFE_INTEGER
            else left = dp[row-1][i-1]
            if(i < 0 || i >= dp[row - 1].length) right = Number.MAX_SAFE_INTEGER
            else right = dp[row-1][i]
            dp[row][i] = Math.min(left, right) + triangle[row][i] 
        }
        row++
    }
    return Math.min(...dp[row - 1])
};