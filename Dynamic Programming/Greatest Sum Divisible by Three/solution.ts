function maxSumDivThree(nums: number[]): number {
    let cache = new Map()
    return helper(nums, 0, 0, cache)
};

function helper(nums, index, remainder, cache) {
    if(index === nums.length) {
        if(remainder === 0) {
            return 0
        } else {
            return Number.MIN_SAFE_INTEGER
        }
    }
    let key = `${index},${remainder}`
    if(cache.has(key)) {
        return cache.get(key)
    }
    let result = Math.max(nums[index] + helper(nums, index + 1, (remainder + nums[index]) % 3, cache), helper(nums, index + 1, remainder, cache))
    cache.set(key, result)
    return result
    
}