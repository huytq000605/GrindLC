function maxProduct(nums: number[]): number {
    let result = nums[0]
    let max = 1
    let min = 1
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] < 0) { // Kadane with modify, when we meet negative, we swap min and max cause change sign
            [max, min] = [min, max]
        }
        max = Math.max(nums[i], max * nums[i])
        min = Math.min(nums[i], min * nums[i])
        result = Math.max(result, max)
        
    }
    return result
};