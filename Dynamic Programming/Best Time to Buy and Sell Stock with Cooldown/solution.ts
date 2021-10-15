function maxProfit(prices: number[]): number {
    let dp = Array(prices.length).fill(0).map(() => Array(2).fill(0).map(() => Array(2)))
    let dfs = (idx: number, cooldown: number, bought: number) => {
        if(idx >= prices.length) return 0
        if(dp[idx][cooldown][bought]) return dp[idx][cooldown][bought]
        let result: number
        if(cooldown === 1) {
            result = dfs(idx + 1, 0, 0) // We cannot do anything
        } else if(bought === 0) {
            result = Math.max(dfs(idx + 1, 0, 1) - prices[idx], dfs(idx + 1, 0, 0)) // We buy or dont do anything
        } else {
            result = Math.max(dfs(idx + 1, 1, 0) + prices[idx], dfs(idx + 1, 0, 1)) // We sell or hold then pass
        }
        dp[idx][cooldown][bought] = result
        return result
    }
    return dfs(0, 0, 0)
};