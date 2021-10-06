function numOfArrays(n: number, m: number, k: number): number {
    let dp = Array(n + 1).fill(0).map(() => Array(m + 1).fill(0).map(() => Array(k + 1)))
    let max = m
    let MOD = 1e9 + 7
    let dfs = (n: number, m: number, k: number) => {
        if(k < 0) dp[n][m][k] = 0
        if(k > n) dp[n][m][k] = 0
        if(dp[n][m][k] !== undefined) return dp[n][m][k]
        if(n === 0) return 1
        let result = 0
        result += dfs(n - 1, m, k) * (m)
        result = result % MOD
        for(let i = m + 1; i <= max; i++) {
            result += dfs(n - 1, i, k - 1)
            result = result % MOD
        }
        result = result % MOD
        dp[n][m][k] = result
        return result
    }
    return dfs(n, 0, k)
    
};