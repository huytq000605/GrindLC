function lastStoneWeightII(stones: number[]): number {
    let half = 0
    for(let stone of stones) {
        half += stone
    }
    half /= 2
    let cache = new Map()
    function helper(index: number, current: number) { // Finding minimum difference to half sum
        if(index === stones.length) return Math.abs(half-current)
        if(current >= half) return Math.abs(half- current)
        const key = `${index},${current}`
        if(cache.has(key)) {
            return cache.get(key)
        }
        let res1 = helper(index + 1, current + stones[index])
        let res2 = helper(index + 1, current)
        cache.set(key, Math.min(res1, res2))
        return cache.get(key)
    }
    return helper(0, 0) * 2
};

