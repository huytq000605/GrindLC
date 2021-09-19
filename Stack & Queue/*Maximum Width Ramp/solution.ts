function maxWidthRamp(nums: number[]): number {
    let result = 0
    let stack = []
    for(let i = 0; i < nums.length; i++) {
        if(stack.length === 0 || nums[stack[stack.length - 1]] > nums[i]) {
            stack.push(i)
        }
    }
    for(let i = nums.length - 1; i >= result; i--) {
        while(stack.length && nums[stack[stack.length -1]] <= nums[i]) {
            result = Math.max(result, i - stack.pop())       
        }
    }
    return result
};