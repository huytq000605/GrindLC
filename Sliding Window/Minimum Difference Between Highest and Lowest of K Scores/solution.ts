function minimumDifference(nums: number[], k: number): number {
    nums.sort((a,b) => a-b)
    let result = Number.MAX_SAFE_INTEGER
    let min = 0
    let max = Math.min(nums.length - 1, k - 1)
    while(max < nums.length) {
        result = Math.min(result, nums[max] - nums[min])
        max++
        min++
    }
    return result
};