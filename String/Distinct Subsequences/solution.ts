function numDistinct(s: string, t: string): number {
    let dp = Array(s.length).fill(0).map(() => Array(t.length))
    let dfs = (idx1, idx2) => {
        if(idx2 >= t.length) return 1
        if(idx1 >= s.length) return 0
        if(dp[idx1][idx2] !== undefined) return dp[idx1][idx2]
        let result = 0
        if(s[idx1] === t[idx2]) {
            result += dfs(idx1 + 1, idx2 + 1)
        }
        result += dfs(idx1 + 1, idx2)
        dp[idx1][idx2] = result
        return result
    }
    
    return dfs(0, 0)
};