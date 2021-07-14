function canPartition(nums: number[]): boolean {
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    let half = sum / 2
    let cache = new Map()
    function helper(index: number, sum: number) {
        if(index === nums.length) {
            if(sum === half) return true
            else return false
        }
        if(sum > half) return false
        const key = `${index},${sum}`
        if(cache.has(key)) return cache.get(key)
        let res1 = helper(index + 1, sum + nums[index])
        let res2 = helper(index + 1, sum)
        cache.set(key, res1 || res2)
        return cache.get(key)
    }
    return helper(0, 0)
};

