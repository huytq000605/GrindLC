function maxSubArray(nums: number[]): number {
    if(nums.length === 1) return nums[0]
    let accSum = Array(nums.length)
    accSum[0] = nums[0]
    for(let i = 1; i < nums.length; i++) {
        accSum[i] = accSum[i-1] + nums[i]
    }
    
    return Math.max(...accSum) - Math.min(...accSum)
    
};