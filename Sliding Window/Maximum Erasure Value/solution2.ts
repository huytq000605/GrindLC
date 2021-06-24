function maximumUniqueSubarray(nums: number[]): number {
    let start = 0;
    let result = 0;
    let sum = 0;
    let map = new Map()
    for(let i = 0; i < nums.length; i++) {
        if(map.has(nums[i]) && map.get(nums[i]) >= start) {
            for(let j = start; j <= map.get(nums[i]); j++) {
                sum -= nums[j]
            }
            start = map.get(nums[i]) + 1
        }
        map.set(nums[i], i)
        sum += nums[i]
        result = Math.max(result, sum)
    }
    return result
};