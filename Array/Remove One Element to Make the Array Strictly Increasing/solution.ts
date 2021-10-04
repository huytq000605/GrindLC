function canBeIncreasing(nums: number[]): boolean {
    let flag = false
    for(let i = 0; i < nums.length - 1; i++) {
        if(nums[i] >= nums[i + 1]) { // There is conflict
            if(!flag) { // If has before => return false
                flag = true
                if(i - 1 >= 0 && nums[i - 1] >= nums[i+1]) { // We try to remove the nums[i], if cannot then try to remove nums[i+1]
                    if(i + 2 < nums.length && nums[i] >= nums[i+2]) return false // Try to remove nums[i+1]
                    else i++ // Bypass nums[i+1]
                }
            } else {
                return false
            }
            
        }
    }
    return true
};