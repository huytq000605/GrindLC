function findUnsortedSubarray(nums: number[]): number {
    let stack = []
    let left = Number.MAX_SAFE_INTEGER
    for(let i = 0; i < nums.length; i++) { // Find the most left that is not sorted
        if(stack.length && nums[i] < nums[stack[stack.length - 1]]) {
            while(stack.length && nums[i] < nums[stack[stack.length - 1]]) {
                left = Math.min(left, stack.pop())
            }
        }
        stack.push(i)
    }
    stack = []
    let right = -1
    for(let i = nums.length - 1; i >= 0; i--) { // Find the most right that is not sorted
        if(stack.length && nums[i] > nums[stack[stack.length - 1]]) {
            while(stack.length && nums[i] > nums[stack[stack.length - 1]]) {
                right = Math.max(right, stack.pop())
            }
        }
        stack.push(i)
    }
    if(right === -1) return 0 // Already sorted
    return right-left + 1
};