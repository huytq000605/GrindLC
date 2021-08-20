function numSubarrayProductLessThanK(nums: number[], k: number): number {
    if(k === 0 || k === 1) return 0
    let currentProduct = 1
    let result = 0
    let j = 0
    for(let i = 0; i < nums.length; i++) {
        currentProduct *= nums[i]
        while(currentProduct >= k) {
            currentProduct /= nums[j++]
        }
        result += i - j + 1
        
    }
    return result
};