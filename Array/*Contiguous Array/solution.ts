function findMaxLength(nums: number[]): number {
    let prefix = Array(nums.length)
    let map = new Map()
    map.set(0, -1)
    for(let i = 0; i < prefix.length; i++) {
        if(nums[i] === 0) nums[i] = -1
        if(i === 0) {
            prefix[i] = nums[i]
        } else {
            prefix[i] = prefix[i - 1] + nums[i]
        }
    }
    let result = 0
    for(let i = 0; i < prefix.length; i++) {
        if(map.has(prefix[i])) {
            result = Math.max(result, i - map.get(prefix[i]))
        }
        if(!map.has(prefix[i])) {
            map.set(prefix[i], i)
        }
    }
    return result
};