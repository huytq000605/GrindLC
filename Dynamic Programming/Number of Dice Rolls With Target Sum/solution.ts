function numRollsToTarget(d: number, f: number, target: number): number {
    let cache = new Map()
    function helper(d: number, f: number, target: number) {
        if(d === 0 && target === 0) return 1
        if(d === 0 && target !== 0) return 0
        const key = `${d},${target}`
        if(cache.has(key)) {
            return cache.get(key)
        }
        let result = 0
        for(let i = 1; i <= f && i <= target; i++) {
            result += helper(d - 1, f, target - i)
        }
        cache.set(key, result % 1000000007)
        return cache.get(key)
    }
    return helper(d, f, target)
    
};

