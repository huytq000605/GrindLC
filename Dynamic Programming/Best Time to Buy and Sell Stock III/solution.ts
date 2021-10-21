function maxProfit(prices: number[]): number {
    let dp = Array(prices.length).fill(0).map(() => Array(2).fill(0).map(() => Array(2)))
    let dfs = (idx, bought, trans) => {
        if(idx >= prices.length || trans === 2) return 0
        if(dp[idx][bought][trans] !== undefined) return dp[idx][bought][trans]
        let result
        if(bought === 0) {
            result = Math.max(dfs(idx + 1, 0, trans), - prices[idx] + dfs(idx + 1, 1, trans))
        } else {
            result = Math.max(dfs(idx + 1, bought, trans), prices[idx] + dfs(idx + 1, 0, trans + 1))
        }
        dp[idx][bought][trans] = result
        return result
    }
    return dfs(0, 0, 0)
};