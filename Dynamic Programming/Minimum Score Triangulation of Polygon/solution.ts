// LIKE 312, 1547
function minScoreTriangulation(values: number[]): number {
    let dp = Array(values.length).fill(0).map(() => Array(values.length))
    let dfs = (start: number, end: number) => {
        if(start + 1 === end) return 0
        if(dp[start][end] !== undefined) return dp[start][end]
        let result = Number.MAX_SAFE_INTEGER
        for(let i = start + 1; i < end; i++) {
            result = Math.min(result, values[start] * values[end] * values[i] + dfs(start, i) + dfs(i, end))
        }
        dp[start][end] = result
        return result
    }
    return dfs(0, values.length - 1)
};