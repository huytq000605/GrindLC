function checkValidString(s: string): boolean {
    let dp = Array(s.length).fill(0).map(() => Array(s.length))
    let dfs = (idx, open) => {
        if(idx >= s.length) {
            if(open === 0) return true
            return false
        }
        if(open < 0) return false
        if(dp[idx][open] !== undefined) return false
        if(s[idx] === "(") {
            dp[idx][open] = dfs(idx + 1, open + 1)
        } else if(s[idx] === ")") {
            dp[idx][open] = dfs(idx + 1, open - 1)
        } else {
            dp[idx][open] = dfs(idx + 1, open + 1)
            if(dp[idx][open]) return true
            dp[idx][open] = dfs(idx + 1, open - 1)
            if(dp[idx][open]) return true
            dp[idx][open] = dfs(idx + 1, open)
        }
        if(dp[idx][open]) return true
        return false
    }
    return dfs(0, 0)
    
};