function sumOfBeauties(nums: number[]): number {
    let maxFromLeft = Array(nums.length).fill(0)
    let minFromRight = Array(nums.length).fill(1e6 + 1)
    for(let i = 0; i < nums.length; i++) {
        if(i === 0) maxFromLeft[i] = nums[0]
        else maxFromLeft[i] = Math.max(maxFromLeft[i-1], nums[i])
    }
    
    for(let i = nums.length - 1; i >= 0; i--) {
        if(i === minFromRight.length - 1) minFromRight[i] = nums[i]
        else minFromRight[i] = Math.min(minFromRight[i+1], nums[i])
    }
    
    let result = 0
    for(let i = 1; i < nums.length - 1; i++) {
        if(nums[i] > maxFromLeft[i-1] && nums[i] < minFromRight[i + 1]) {
            result += 2
        } else if(nums[i] > nums[i-1] && nums[i] < nums[i + 1]) {
            result++
        }
    }
    return result
};