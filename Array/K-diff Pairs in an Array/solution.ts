function findPairs(nums: number[], k: number): number {
    let map = new Map()
    for(let num of nums) {
        map.set(num, (map.get(num) || 0) + 1)
    }
    let result = 0
    if(k === 0) {
        for(let [num, freq] of map.entries()) {
            if(freq >= 2) {
                result++
            }
        }
    } else {
        for(let num of map.keys()) {
            if(map.has(k + num)) result++
        }
    }
    
    return result
};