function subsetsWithDup(nums: number[]): number[][] {
    let result = [[]]
    nums.sort((a,b) => a-b)
    helper(nums, 0, [], result)
    return result
}

function helper(nums, index, current, result) {
    if(index === nums.length) return
    current.push(nums[index])
    result.push([...current])
    helper(nums, index + 1, current, result)
    current.pop()
    let added = nums[index]
    while(added === nums[index]) {
        index++
    }
    helper(nums, index, current, result)
}