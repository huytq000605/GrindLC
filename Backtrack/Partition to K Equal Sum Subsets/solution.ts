function canPartitionKSubsets(nums: number[], k: number): boolean {
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    if(sum % k !== 0) return false
    nums.sort((a,b) => b-a)
    let target = sum / k
    for(let num of nums) {
        if(num > target) return false
    }
    let indexUsed = Array(nums.length).fill(false)
    const helper = (current: number, groups: number) => {
        if(current > target) return false
        if(current === target) {
            groups--
            if(groups === 0) {
                for(let i = 0; i < indexUsed.length; i++) {
                   if(indexUsed[i] === false) return false
                }
                return true
            }
            current = 0
        }
        
        for(let i = 0; i < nums.length; i++) {
            
            if(indexUsed[i]) continue
            indexUsed[i] = true
            if(helper(current + nums[i], groups)) return true
            indexUsed[i] = false
        }
        return false
    }
    
    return helper(0, k)
};