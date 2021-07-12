function combine(n: number, k: number): number[][] {
    let result = []
    let nums = Array(n).fill(0).map((_, idx) => idx + 1)
    helper(nums, 0, k, [], result)
    return result
};

function helper(nums: number[], index: number, k: number, current: number[], result: number[][]) {
    if(current.length === k) {
        result.push([...current])
    }
    for(let i = index; i < nums.length; i++) {
        current.push(nums[i])
        helper(nums, i + 1, k, current, result)
        current.pop()
    }
}