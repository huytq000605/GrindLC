function minIncrementForUnique(nums: number[]): number {
    nums.sort((a,b) => a-b)
    let result = 0
    let need = Number.MIN_SAFE_INTEGER
    let set = new Set()
    for(let num of nums) {
        if(set.has(num)) {
            result += need - num
            num = need
        }
        set.add(num)
        need = num + 1
    }
    return result
    
};