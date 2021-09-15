function jump(nums: number[]): number {
    let dp = Array(nums.length).fill(Number.MAX_SAFE_INTEGER)
    dp[0] = 0
    for(let i = 0; i < nums.length; i++) {
        for(let j = 1; j <= nums[i]; j++) {
            dp[i + j] = Math.min(dp[i] + 1, dp[i + j])
        }
    }
    return dp[nums.length - 1]
    
};