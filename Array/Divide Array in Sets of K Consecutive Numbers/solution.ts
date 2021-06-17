function isPossibleDivide(nums: number[], k: number): boolean {
    let freq = new Map()
    nums.sort((a,b) => a-b)
    let indexUsed = new Map()
    for(let i = 0; i < nums.length; i++) {
        if(!freq.get(nums[i])) {
            freq.set(nums[i], [])
        }
        freq.get(nums[i]).push(i)
    }
    
    for(let i = 0; i < nums.length; i++) {
        if(indexUsed.get(i)) {
            continue
        }
        let currentValue = nums[i]
        for(let j = 0; j < k; j++) {
            let idxCurrentValue = freq.get(currentValue)
            if(idxCurrentValue && idxCurrentValue.length > 0) {
                let used = idxCurrentValue.shift()
                indexUsed.set(used, true)
                currentValue++
            } else {
                return false
            }
                
        }
    }
    return true
};