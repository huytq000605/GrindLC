function minCost(n: number, cuts: number[]): number {
    cuts.sort((a,b) => a-b)
    cuts = [0, ...cuts, n]
    let dp = Array(cuts.length).fill(0).map(() => Array(cuts.length))
    
    let dfs = (start, end) => {
        if(start + 1 === end) {
            return 0
        }
        if(dp[start][end] !== undefined) return dp[start][end]
        let result = Number.MAX_SAFE_INTEGER
        for(let i = start + 1; i < end; i++) {
            result = Math.min(result, cuts[end] - cuts[start] + dfs(start, i) + dfs(i, end))
        }
        dp[start][end] = result
        return result
    }
    
    return dfs(0, cuts.length - 1)
};