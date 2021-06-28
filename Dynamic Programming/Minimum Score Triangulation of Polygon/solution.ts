function minScoreTriangulation(values: number[]): number {
    let map = new Map()
    return helper(values, 0, values.length -1, map)
};

function helper(nums: number[], start: number, end: number, map: Map<string, number>): number {
    const key = `${start}-${end}`
    if(map.has(key)) {
        return map.get(key)
    }
    if(end - start + 1 < 3) {
        return 0
    }
    let result = Number.MAX_SAFE_INTEGER
    for(let i = start + 1; i < end; i++) {
        result = Math.min(result, nums[start]*nums[end]*nums[i] + helper(nums, start, i, map) + helper(nums, i, end, map))
    }
    map.set(key, result)
    return result
}