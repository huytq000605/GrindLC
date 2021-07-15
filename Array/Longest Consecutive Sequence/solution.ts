function longestConsecutive(nums: number[]): number {
    let result = 0
    let have = new Set<number>()
    for(let num of nums) {
        have.add(num)
    }
    for(let num of nums) {
        if(!have.has(num)) continue
        result = Math.max(result, dfs(num, have))
    }
    return result
    
};

function dfs(num: number, set: Set<number>) {
    set.delete(num)
    let left = set.has(num - 1) ? dfs(num - 1, set) : 0
    let right = set.has(num + 1) ? dfs(num + 1, set) : 0
    return 1 + left + right
}