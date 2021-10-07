function longestDecomposition(text: string): number {
    let dp = Array(text.length).fill(0).map(() => Array(text.length))
    let dfs = (i: number, j: number) => {
        if(i > j) {
            return 0
        }
        if(i === j) {
            return 1
        }
        if(dp[i][j] !== undefined) return dp[i][j]
        let left = i
        let right = j
        let result = 1
        while(left < right) {
            if(text.slice(i, left + 1) === text.slice(right, j + 1)) {
                result = Math.max(result, 2 + dfs(left + 1, right - 1) )
            }
            left++
            right--
        }
        dp[i][j] = result
        return result
    }
    return dfs(0, text.length - 1)
};