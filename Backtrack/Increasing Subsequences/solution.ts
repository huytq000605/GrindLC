function findSubsequences(nums: number[]): number[][] {
    let result = []
    helper(nums, 0 , [], result)
    return result
};

function helper(nums: number[], index: number, current: number[], result: number[][]) {
    if(current.length >= 2) result.push([...current])
    if(index === nums.length) return
    let set = new Set()
    for(let i = index; i < nums.length; i++) {
        if(set.has(nums[i]) || current.length > 0 && nums[i] < current[current.length - 1]) continue
        set.add(nums[i])
        current.push(nums[i])
        helper(nums, i + 1, current, result)
        current.pop()
    }
}