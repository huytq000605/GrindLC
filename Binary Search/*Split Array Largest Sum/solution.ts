function splitArray(nums: number[], m: number): number {
    let min: number = 0
    let max: number = 0
    for(let num of nums) {
        min = Math.max(min, num)
        max += num
    }
    
    let valid = (sum: number) => {
        let group = 0
        let curr = 0
        for(let num of nums) {
            if(curr + num > sum) {
                curr = num
                group++
                if(group >= m) return false
            } else {
                curr += num
            }
        }
        return true
    }
    
    while(min < max) {
        let sum = min + Math.floor((max - min) / 2)
        if(valid(sum)) {
            max = sum
        } else {
            min = sum + 1
        }
    }
    return min
};