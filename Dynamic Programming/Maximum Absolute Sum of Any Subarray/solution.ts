/*
Find min subarray and max subarray => use kadane's algorithm 2 times
*/

function maxAbsoluteSum(nums: number[]): number {
    let dpMax = Array(nums.length)
    let dpMin = Array(nums.length)
    dpMax[0] = nums[0]
    dpMin[0] = nums[0]
    for(let i = 1; i < nums.length; ++i) {
        dpMax[i] = Math.max(dpMax[i-1] + nums[i], nums[i])
    }
    let maxSum = Math.max(...dpMax)
    for(let i = 1; i < nums.length; ++i) {
        dpMin[i] = Math.min(dpMin[i-1] + nums[i], nums[i])
    }
    let minSum = Math.min(...dpMin)
    return Math.max(Math.abs(maxSum), Math.abs(minSum))
};