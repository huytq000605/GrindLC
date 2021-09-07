function getMaxLen(nums: number[]): number {
    let result = 0
    let start = 0
    let firstNegative = 0
    let lastNegative = 0
    let countNegative = 0
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] === 0) {
            if(countNegative % 2 === 0) {
                result = Math.max(result, i - 1 - start + 1)
            } else {
                result = Math.max(result, lastNegative - 1- start + 1, i - 1 - (firstNegative + 1) + 1)
            }
            countNegative = 0
            start = i + 1
        } else {
            if(nums[i] < 0) {
                if(countNegative === 0) firstNegative = i
                lastNegative = i
                countNegative++
            }
        }
    }
    // last break is nums.length - 1
    if(countNegative % 2 === 0) {
        result = Math.max(result, nums.length - 1 - start + 1)
    } else {
        result = Math.max(result, lastNegative - 1- start + 1, nums.length - 1 - (firstNegative + 1) + 1)
    }
    
    return result
};