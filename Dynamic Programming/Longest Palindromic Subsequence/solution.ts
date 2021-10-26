function longestPalindromeSubseq(s: string): number {
    let dp = Array(s.length).fill(0).map(() => Array(s.length))
    let dfs = (left: number, right: number) => {
        if(left > right) {
            return 0
        }
        if(left === right) {
            return 1
        }
        if(dp[left][right] !== undefined) return dp[left][right]
        let result
        if(s[left] === s[right]) {
            result = dfs(left + 1, right - 1) + 2
        } else {
            result = Math.max(dfs(left + 1, right), dfs(left, right - 1))
        }
        dp[left][right] = result
        return result
    }
    return dfs(0, s.length - 1)
}