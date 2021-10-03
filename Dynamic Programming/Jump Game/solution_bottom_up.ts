// Actually can solve with O(n) Greedy
function canJump(nums: number[]): boolean {
    if(nums.length === 1) return true
    let dp = Array(nums.length)
    dp[0] = nums[0]
    for(let i = 0; i < nums.length; i++) {
        if(dp[i] === undefined) continue
        for(let j = 1; j <= dp[i] && i + j < nums.length; j++) {
            dp[i + j] = nums[i+j]
            if(i + j === nums.length -1) return true
        }
    }
    return false
    
};