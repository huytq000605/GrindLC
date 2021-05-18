function subsets(nums: number[]): number[][] {
    let result = [[]]
    for (let i = 0; i < nums.length; i++) {
        let current = []
        helper(nums, i, current, result)
    }
    
    return result
}

function helper(nums: number[], idx: number, current: number[], result: number[][]): void {
    if (idx == nums.length) {
      return  
    } 
    current.push(nums[idx]);
    result.push([...current])
    for (let i = idx + 1; i < nums.length; i++) {
        let ori = [...current]
        helper(nums, i, current, result)
        current = ori
    }
}