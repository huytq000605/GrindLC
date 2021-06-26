function rob(nums: number[]): number {
    let cache = new Map()
    function helper(index) {
        if(index >= nums.length) {
            return 0
        }
        if(cache.has(index)) {
            return cache.get(index)
        }
        let robThis = nums[index] + helper(index + 2)
        let passThis = helper(index + 1)
        cache.set(index, Math.max(robThis, passThis))
        return cache.get(index)
    }
    return helper(0)
};