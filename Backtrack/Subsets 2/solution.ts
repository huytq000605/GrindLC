function subsetsWithDup(nums: number[]): number[][] {
    let result = []
    nums.sort((a,b) => a-b)
    helper(nums, 0, [], result)
    return result
}

function helper(nums: number[], index: number, current: number[], result: number[][]) {
    result.push([...current])
    if(index === nums.length) return
    while(index < nums.length) {
        current.push(nums[index])
        helper(nums, index + 1, current, result)
        current.pop()
        let added = nums[index]
        while(nums[index] === added) {
            index++
        }
    }
}