function findNumberOfLIS(nums: number[]): number {
    let dp = Array(nums.length).fill(0).map(() => Array(2).fill(0)) // dp[i] is a 2 elements array, first one is length, second one is count
    let maxLen = 0
    let count = 0
    for(let i = 0; i < nums.length; i++) {
        dp[i] = [1,1]
        for(let j = 0; j < i; j++) {
            if(nums[j] < nums[i]) {
                if(dp[j][0] >= dp[i][0]) {
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = dp[j][1]
                } else if(dp[j][0] === dp[i][0] - 1) {
                    dp[i][1] += dp[j][1]
                }
            }
        }
        if(maxLen < dp[i][0]) {
            maxLen = dp[i][0]
            count = dp[i][1]
        } else if(maxLen === dp[i][0]) {
            count += dp[i][1]
        }
    }
    return count
};