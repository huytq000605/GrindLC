function numSquares(n: number): number {
    let dp = Array(n + 1).fill(Number.MAX_SAFE_INTEGER)
    dp[0] = 0
    for(let i = 1; i <= n; i++) {
        for(let j = 1; j * j <= i; j++) {
            dp[i] = Math.min(dp[i], 1 + dp[i - j*j])
        }
    }
    return dp[n]
};
