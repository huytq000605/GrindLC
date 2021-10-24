function isMatch(s: string, p: string): boolean {
    let dp = Array(s.length).fill(0).map(() => Array(p.length))
    let dfs = (idx1, idx2) => {
        if(idx1 >= s.length && idx2 >= p.length) return true
        if(idx2 >= p.length) return false
        if(idx1 >= s.length) {
            for(let i = idx2; i < p.length; i++) {
                if(p[i] !== "*") return false
            }
            return true
        }
        if(dp[idx1][idx2] !== undefined) return dp[idx1][idx2]
        let result
        if(p[idx2] === "?") {
            result = dfs(idx1 + 1, idx2 + 1)
        } else if(p[idx2] === "*") {
            for(let i = 0; i < s.length - idx1 + 1; i++) {
                if(dfs(idx1 + i, idx2 + 1)) return true
            }
            result = false
        } else if(s[idx1] === p[idx2]) {
            result = dfs(idx1 + 1, idx2 + 1)
        } else {
            result = false
        }
        dp[idx1][idx2] = result
        return result
    }
    
    return dfs(0, 0)
};