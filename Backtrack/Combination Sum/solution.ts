function combinationSum(candidates: number[], target: number): number[][] {
    let result = []
    helper(candidates, target, 0, [], result)
    return result
}

function helper(nums: number[], target: number, index: number, current: number[], result: number[][]) {
    if(target === 0) {
        result.push([...current])
        return
    }
    if(target < 0 || index === nums.length) {
        return 
    }
    current.push(nums[index]) // We push the current index of nums to current
    helper(nums, target - nums[index], index, current, result)
    current.pop()
    
    helper(nums, target, index + 1, current, result) // We pass the current index of nums
}