function isInterleave(s1: string, s2: string, s3: string): boolean {
    if(s1.length + s2.length !== s3.length) return false
    let dp = Array(s1.length + 1).fill(0).map(() => Array(s2.length + 1))
    let dfs = (idx1, idx2) => {
        if(idx1 + idx2 === s3.length) {
            return true
        }
        if(dp[idx1][idx2] !== undefined) return dp[idx1][idx2]
        if(idx1 < s1.length && s1[idx1] === s3[idx1 + idx2]) {
            if(dfs(idx1 + 1, idx2)) return true
        }
        if(idx2 < s2.length && s2[idx2] === s3[idx1 + idx2]) {
            if(dfs(idx1, idx2 + 1)) return true
        }
        dp[idx1][idx2] = false
        return false
    }
    return dfs(0, 0)
    
};