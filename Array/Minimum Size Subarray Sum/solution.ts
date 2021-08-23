function minSubArrayLen(target: number, nums: number[]): number {
    let sum = 0
    let start = 0
    let result = Number.MAX_SAFE_INTEGER
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i]
        while(sum >= target) {
            result = Math.min(result, i - start + 1)
            sum -= nums[start]
            start++
        }
    }
    if(result === Number.MAX_SAFE_INTEGER) return 0
    return result
};