function maxFrequency(nums: number[], k: number): number {
    nums.sort((a,b) => a-b)
    let start = 0
    let sum = 0
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i]
        while(nums[i] * (i - start + 1) - sum > k) {
            sum -= nums[start]
            start++
        }
        result = Math.max(result, i - start + 1)
    }
    return result
};