function isMatch(s: string, p: string): boolean {
    let dp = Array(p.length).fill(0).map(() => Array(s.length))
    let dfs = (idx1, idx2) => {
        if(idx1 >= p.length && idx2 >= s.length) return true
        if(idx2 >= s.length) {
            if((p.length - idx1) % 2 === 1) return false
            for(let i = idx1 + 1; i < p.length; i+=2) {
                if(p[i] !== "*") return false
            }
            return true
        }
        if(idx1 >= p.length) return false
        if(dp[idx1][idx2] !== undefined) return dp[idx1][idx2]
        let result
        if(idx1 < p.length - 1 && p[idx1 + 1] === "*") {
            let currentPChar = p[idx1]
            if(dfs(idx1 + 2, idx2)) return true
            for(let i = 0; i < s.length - idx2 + 1 && (currentPChar === "." || currentPChar === s[idx2 + i]); i++) {
                if(dfs(idx1 + 2, idx2 + i + 1)) return true
            }
            result = false
        } else if(p[idx1] === ".") {
            result = dfs(idx1 + 1, idx2 + 1)
        } else if(p[idx1] === s[idx2]) {
            result = dfs(idx1 + 1, idx2 + 1)
        } else {
            result = false
        }
        dp[idx1][idx2] = result
        return result
    }
    return dfs(0, 0)
};