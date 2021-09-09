function rob(nums: number[]): number {
    if(nums.length === 1) return nums[0]
    let dp = Array(nums.length).fill(0).map(() => Array(2))
    let dfs = (idx, first) => {
        if(idx >= nums.length - 1 && first === 1) {
            return 0
        }
        if(idx >= nums.length) {
            return 0
        }
        if(dp[idx][first] !== undefined) return dp[idx][first]
        let robThis = nums[idx] + dfs(idx + 2, first)
        let passThis = dfs(idx + 1, first)
        dp[idx][first] = Math.max(robThis, passThis)
        return dp[idx][first]
    }
    
    return Math.max(dfs(0, 1), dfs(1, 0))
};