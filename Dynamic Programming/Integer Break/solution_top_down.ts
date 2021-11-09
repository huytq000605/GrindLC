function integerBreak(n: number): number {
    let given = n
    let dp = Array(n)
    let dfs = (n) => {
        if(n === 1) return 1
        if(dp[n] !== undefined) return dp[n]
        let result = n
        if(n === given) result = 0
        for(let i = 1; i < n; i++) {
            result = Math.max(result, dfs(i) * dfs(n - i))
        }
        dp[n] = result
        return result
    }
    return dfs(n)
    
};