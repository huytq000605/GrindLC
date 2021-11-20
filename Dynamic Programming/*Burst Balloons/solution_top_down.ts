function maxCoins(nums: number[]): number {
    nums = [1, ...nums, 1]
    let dp = Array(nums.length).fill(0).map(() => Array(nums.length))
    // dp[i][j] is mean burst baloons the way that nums[i] => nums[j] are the last baloons to burst
    let dfs = (start, end) => {
        if(start > end) return 0
        if(dp[start][end] !== undefined) return dp[start][end]
        let result = Number.MIN_SAFE_INTEGER
        let left = nums[start - 1]
        let right = nums[end + 1]
        for(let i = start; i <= end; i++) {
            result = Math.max(result, left * nums[i] * right + dfs(start, i - 1) + dfs(i + 1, end))
        }
        dp[start][end] = result
        return result
    }
    return dfs(1, nums.length - 2)
};