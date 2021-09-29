// Find the longest subarray have sum = (sum(nums) - x)
function minOperations(nums: number[], x: number): number {
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    let target = sum - x
    sum = 0
    let result = Number.MAX_SAFE_INTEGER
    let map = new Map()
    map.set(0, -1)
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i]
        if(!map.has(sum)) map.set(sum, i)
        if(map.has(sum - target)) {
            let idx = map.get(sum - target)
            result = Math.min(result, nums.length - (i - idx))
        }
        
    }
    if(result === Number.MAX_SAFE_INTEGER) result = -1
    return result
};