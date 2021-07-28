function canPartition(nums: number[]): boolean {
    nums.sort((a,b) => a-b)
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    let cache = new Map()
    function helper(index: number, current: number) {
        const key = `${index},${current}`
        if(cache.has(key)) return cache.get(key)
        if(current > sum / 2) return false
        if(current === sum / 2) return true
        if(index === nums.length) return false
        if(helper(index + 1, current + nums[index])) {
            cache.set(key, true)
            return true
        }
    
        if(helper(index + 1, current)) {
        cache.set(key, true)
        return true
        } 
   
        cache.set(key, false)
        return false
    }
    return helper(0, 0)
};

