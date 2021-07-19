function movesToMakeZigzag(nums: number[]): number {
    if(nums.length < 3) return 0
    
    let evenIndexGreater = 0
    
    for(let i = 1; i < nums.length; i+= 2) {
        let prev = i - 1
        let next = i + 1
        if(next >= nums.length) next = prev
        let min = Math.min(nums[prev], nums[next])
        if(nums[i] >= min) {
            evenIndexGreater += nums[i] - min + 1
        }
    }
    
    let oddIndexGreater = 0
    
    for(let i = 0; i < nums.length; i+= 2) {
        let prev = i - 1
        let next = i + 1
        if(prev < 0) prev = next
        if(next >= nums.length) next = prev
        let min = Math.min(nums[prev], nums[next])
        if(nums[i] >= min) {
            oddIndexGreater += nums[i] - min + 1
        }
    }
    
    return Math.min(oddIndexGreater, evenIndexGreater)
};