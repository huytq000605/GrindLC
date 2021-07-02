function subarraySum(nums: number[], k: number): number {
    let prefix = Array(nums.length + 1).fill(0)
    for(let i = 1; i < prefix.length; i++) {
        prefix[i] = nums[i - 1] + prefix[i-1] 
    }
    let result = 0
    let map = new Map()
    for(let i = 1; i < prefix.length; i++) {
        if(prefix[i] === k) {
            result++
        }
        if(map.has(prefix[i] - k)) {
            result += map.get(prefix[i] - k)
        }
        map.set(prefix[i], (map.get(prefix[i]) || 0) + 1)
    }
    return result
};