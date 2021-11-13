function maxProfit(k: number, prices: number[]): number {
    let dp = Array(prices.length).fill(0).map(() => Array(k + 1).fill(0).map(() => Array(2)))
    let dfs = (idx, k, inTrans) => {
        if(idx >= prices.length) {
            return 0
        }
        if(k === 0 && inTrans === 0) {
            return 0
        }
        if(dp[idx][k][inTrans] !== undefined) return dp[idx][k][inTrans]
        let result
        if(inTrans) {
            result = prices[idx] + dfs(idx + 1, k, 0)
        } else {
            result = -prices[idx] + dfs(idx + 1, k - 1, 1)
        }
        result = Math.max(result, dfs(idx + 1, k, inTrans))
        dp[idx][k][inTrans] = result
        return result
    }
    return dfs(0, k, 0)
};