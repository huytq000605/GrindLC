function reductionOperations(nums: number[]): number {
    nums.sort((a,b) => b-a)
    let numOfNumber = 0
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        if(i > 0 && nums[i] !== nums[i-1]) result += numOfNumber
        numOfNumber++
    }
    return result
}