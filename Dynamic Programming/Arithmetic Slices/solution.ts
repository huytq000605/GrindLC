function numberOfArithmeticSlices(nums: number[]): number {
    if(nums.length < 3) return 0
    let result = 0;
    let dp = Array(nums.length).fill(0)
    if(nums[2] - nums[1] == nums[1] - nums[0]) {
        dp[2] = 1
    }
    result = dp[2]
    
    for(let i = 3; i < nums.length; i++) {
        if(nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
            dp[i] = dp[i-1] + 1
            result += dp[i]
        }
    }
    return result
};