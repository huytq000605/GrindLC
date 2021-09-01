function arrayNesting(nums: number[]): number {
    let seen = new Set()
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        let current = i
        let res = 0
        while(true) {
            if(seen.has(current)) break
            seen.add(current)
            res++
            result = Math.max(result, res)
            current = nums[current]
        }
    }
    return result
};