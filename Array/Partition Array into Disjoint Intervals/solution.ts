function partitionDisjoint(nums: number[]): number {
    let maxFromLeft = Array(nums.length).fill(Number.MIN_SAFE_INTEGER)
    let minFromRight = Array(nums.length).fill(Number.MAX_SAFE_INTEGER)
    for(let [index, num] of nums.entries()) {
        maxFromLeft[index] = Math.max(maxFromLeft[index - 1] || Number.MIN_SAFE_INTEGER, num)
    }
    for(let i = nums.length - 1; i >= 0; i--) {
        minFromRight[i] = Math.min(minFromRight[i + 1] === undefined ? Number.MAX_SAFE_INTEGER: minFromRight[i+1], nums[i])
    }
   
    for(let i = 0; i < nums.length - 1; i++) {
        if(maxFromLeft[i] <= minFromRight[i + 1]) {
            return i + 1
        }
    }
    return 0
};