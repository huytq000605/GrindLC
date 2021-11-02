function maxProfit(prices: number[]): number {
    let dp = Array(prices.length).fill(0).map(() => Array(2))
    let dfs = (idx, hold) => {
        if(idx >= prices.length) return 0
        if(dp[idx][hold] !== undefined) return dp[idx][hold]
        let result
        if(hold === 0) {
            result = Math.max(-prices[idx] + dfs(idx + 1, 1), dfs(idx + 1, 0))
        } else {
            result = Math.max(prices[idx] + dfs(idx + 1, 0), dfs(idx + 1, 1))
        }
        dp[idx][hold] = result
        return result
    }
    return dfs(0, 0)
};