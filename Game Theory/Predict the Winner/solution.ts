function PredictTheWinner(nums: number[]): boolean {
    let cache = {}
    let diffPoints = helper(nums, 0, nums.length - 1, true, cache)
    if(diffPoints >= 0) {
        return true
    }
    return false
};

function helper(nums: number[], start: number, end: number, p1Turn: boolean, cache: Object): number {
    if(start > end) {
        return 0
    }
    const key = `${start}-${end}-${p1Turn}`
    if(cache[key]) {
        return cache[key]
    }
    let getFirst: number
    let getLast: number
    if(p1Turn) { // We need to get maximum point for player 1
        getFirst = nums[start] + helper(nums, start + 1, end, !p1Turn, cache)
        getLast = nums[end] + helper(nums, start, end - 1, !p1Turn, cache)
        cache[key] = Math.max(getFirst, getLast)
        return cache[key]
    } else { // We need to get maximum point for player 2
        getFirst = -nums[start] + helper(nums, start + 1, end, !p1Turn, cache)
        getLast = -nums[end] + helper(nums, start, end - 1, !p1Turn, cache)
        cache[key] = Math.min(getFirst, getLast)
        return cache[key]
    }
    
}