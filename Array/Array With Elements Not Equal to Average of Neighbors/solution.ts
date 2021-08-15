function rearrangeArray(nums: number[]): number[] {
    nums.sort((a,b) => a-b)
    let bigStart: number
    if(nums.length % 2 === 0) {
        bigStart = nums.length / 2
    } else {
        bigStart = Math.floor(nums.length / 2) + 1
    }
    let result = []
    let i = 0
    let j = bigStart
    while(i < bigStart) {
        result.push(nums[i++])
        if(j < nums.length) {
            result.push(nums[j++])
        }
        
    }
    return result
}; 