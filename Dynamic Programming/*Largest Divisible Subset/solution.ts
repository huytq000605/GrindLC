// Like LIS
function largestDivisibleSubset(nums: number[]): number[] {
    nums.sort((a,b) => a-b)
    let dp = Array(nums.length).fill(1).map((e, i) => [nums[i]])
    for(let i = 0; i < nums.length; i++) {
        for(let j = 0; j < i; j++) {
            if(nums[i] % nums[j] === 0 && dp[j].length + 1 > dp[i].length) {
                dp[i] = [...dp[j], nums[i]]
            }
        }
    }
    let result = []
    for(let i = 0; i < dp.length; i++) {
        if(result.length < dp[i].length) {
            result = dp[i]
        }
    }
    return result
};