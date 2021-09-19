/*
Just one more typical question about monotonous stack, the tricky of this question is to finding next greater element but can search circularly
so we just loop through it 2 times, remember to module the index
*/

function nextGreaterElements(nums: number[]): number[] {
    let result = Array(nums.length).fill(-1)
    let stack = []
    for(let i = 0; i < nums.length * 2; i++) {
        while(stack.length && nums[i % nums.length] > nums[stack[stack.length - 1]]) {
            result[stack.pop()] = nums[i%nums.length] 
        }
        stack.push(i%nums.length)
    }
    return result;
};