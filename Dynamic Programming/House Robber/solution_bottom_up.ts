function rob(nums: number[]): number {
    let dp = Array(nums.length).fill(0)
    dp[0] = nums[0]
    if(nums.length === 1) return dp[0]
    dp[1] = Math.max(nums[1], dp[0])
    for(let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i-2] + nums[i])   
    }
    return dp[dp.length - 1]
    
};