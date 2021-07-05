function maxSumDivThree(nums: number[]): number {
    nums.sort((a,b) => a-b)
    let result = 0
    let remain2 = []
    let remain1 = []
    for(let i = nums.length -1; i >= 0; i--) {
        if(nums[i] % 3 === 0) {
            result += nums[i]
        }
        if(nums[i] % 3 === 1) {
            remain1.push(nums[i])
        }
        if(nums[i] % 3 === 2) {
            remain2.push(nums[i])
        }
        if(remain1.length && remain2.length) {
            result += remain1.shift() + remain2.shift()
        }
        if(remain1.length === 3){
            while(remain1.length) {
                result += remain1.pop()
            }
        }
        if(remain2.length === 3) {
            while(remain2.length) {
                result += remain2.pop()
            }
        }
    }
    return result
};
    