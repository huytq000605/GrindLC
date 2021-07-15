function canChoose(groups: number[][], nums: number[]): boolean {
    let currentGroup = 0
    let idx = 0
    while(idx < nums.length) {
        if(nums[idx] === groups[currentGroup][0]) {
            let matched = true
            if(idx + groups[currentGroup].length - 1 >= nums.length) {
                return false
            } else {
                for(let i = 1; i < groups[currentGroup].length; i++) {
                    if(nums[idx + i] !== groups[currentGroup][i]) {
                        matched = false
                        break
                    }
                }
                if(matched) {
                    if(currentGroup === groups.length - 1) return true
                    idx += groups[currentGroup].length - 1
                    currentGroup++
                }
            }
        }
        idx++
    }
    return false
};