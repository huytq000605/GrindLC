function deleteAndEarn(nums: number[]): number {
    let cache = new Map()
    nums.sort((a,b) => a-b)
    function helper(index: number) {
        if(index >= nums.length ) {
            return 0
        }
        let key = index
        if(cache.has(key)) {
            return cache.get(key)
        }
        let currentValue = nums[index]
        let getThis = 0
        while(index < nums.length && nums[index] === currentValue) {
            getThis += currentValue
            index += 1
        }
        let passThis = helper(index)
        let nextValue = currentValue + 1
        while(index < nums.length && nums[index] === nextValue) {
            index += 1
        }
        getThis += helper(index)
        cache.set(key, Math.max(getThis, passThis))
        return cache.get(key)   
    }
    return helper(0)
};

