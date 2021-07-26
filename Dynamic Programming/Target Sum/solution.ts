function findTargetSumWays(nums: number[], target: number): number {
    let cache = new Array(nums.length).fill(0).map(() => Array(2000))
    function helper(index: number, num: number) {
    if(index === nums.length) {
        if(num === target) return 1
        else return 0
    }
    if(cache[index][num] !== undefined) {
        return cache[index][num]
    }
    cache[index][num] = helper(index + 1, num + nums[index]) + helper(index + 1, num - nums[index])
    return cache[index][num]
    
}
    return helper(0, 0)
};

