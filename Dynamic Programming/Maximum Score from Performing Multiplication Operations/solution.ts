function maximumScore(nums: number[], multipliers: number[]): number {
    let dp = Array(multipliers.length).fill(0).map(() => Array(multipliers.length))
    let dfs = (idx: number, left: number) => {
        if(idx >= multipliers.length) return 0
        if(dp[idx][left] !== undefined) return dp[idx][left]
        let result = Math.max(dfs(idx + 1, left + 1) + multipliers[idx] * nums[left], dfs(idx + 1, left) + multipliers[idx] * nums[nums.length - 1 - (idx-left)])
        dp[idx][left] = result
        return result
    }
    return dfs(0, 0)
};