function countMaxOrSubsets(nums: number[]): number {
    let max = 0
    for(let num of nums) {
        max |= num
    }
    let result = 0
    // Generate all subset equal to max
    let countSubset = (idx, current) => {
        for(let i = idx ; i < nums.length; i++) {
            if((current | nums[i]) === max) result++
            countSubset(i + 1, current | nums[i])
        }
    }
    
    countSubset(0, 0)
    return result
};