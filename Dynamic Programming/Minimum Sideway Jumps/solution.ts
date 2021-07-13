function minSideJumps(obstacles: number[]): number {
    let cache = Array(3).fill(0).map(() => Array(obstacles.length))
    function helper(current: number, index: number) { // current is road [0, 1, 2] => [1, 2, 3]
        if(index === obstacles.length - 1) return 0
        if(cache[current][index] !== undefined) return cache[current][index] 
        let result = Number.MAX_SAFE_INTEGER
        if(obstacles[index  + 1] === current + 1) {
            for(let i = 0; i <= 2; i++) {
                if(i === current) continue
                if(obstacles[index] === i + 1) continue
                result = Math.min(result, 1 + helper(i, index + 1))
            }
        } else {
            result = helper(current, index + 1)
        }
        cache[current][index] = result
        return result
    }
    return helper(1, 0)
        
};

