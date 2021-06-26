function numPairsDivisibleBy60(time: number[]): number {
    let map = new Map()
    for(let t of time) {
        map.set(t%60, (map.get(t%60) || 0) + 1)
    }
    let result = 0;
    for(let [key,value] of map.entries()) {
        if(key === 30 || key === 0) {
            result += value * (value - 1) / 2
            map.delete(key)
            continue
        }
        result += value * (map.get(60 - key) || 0)
        map.delete(key)
        map.delete(60-key)
    }
    return result
};