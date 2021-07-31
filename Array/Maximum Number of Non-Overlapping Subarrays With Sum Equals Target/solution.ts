function maxNonOverlapping(nums: number[], target: number): number {
    let prefixSumMap = new Set()
    let sum = 0
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i]
        if(nums[i] === target || sum === target || prefixSumMap.has(sum - target)) {
            result++
            sum = 0
            prefixSumMap.clear()
            continue
        }
        prefixSumMap.add(sum)
    }
    return result
};