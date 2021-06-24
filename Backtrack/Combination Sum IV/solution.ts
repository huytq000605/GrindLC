function combinationSum4(nums: number[], target: number): number {
    let cache = new Map()
    return helper(nums, target, cache)
};

function helper(nums: number[], target: number, cache: Map<number, number>) {
    if(cache.has(target)) {
        return cache.get(target)
    }
    if(target === 0) {
        return 1
    }
    let result = 0
    for(let num of nums) {
        if(target >= num) {
            result += helper(nums, target - num, cache)
        }
    }
    cache.set(target, result)
    return result
    
    
}