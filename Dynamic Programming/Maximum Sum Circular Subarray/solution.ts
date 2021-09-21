function maxSubarraySumCircular(nums: number[]): number {
    let maxSubarray = Array(nums.length).fill(0)
    let minSubarray = Array(nums.length).fill(0)
    maxSubarray[0] = nums[0]
    minSubarray[0] = nums[0]
    let sum = nums[0]
    for(let i = 1; i < nums.length; i++) {
        maxSubarray[i] = Math.max(maxSubarray[i-1] + nums[i], nums[i])
        minSubarray[i] = Math.min(minSubarray[i-1] + nums[i], nums[i])
        sum += nums[i]
    }

    let max = Math.max(...maxSubarray)
    let min = Math.min(...minSubarray)
    
    if(max < 0) return max // All number is < 0
    
    return Math.max(max, sum - min)
};