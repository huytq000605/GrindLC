function mostCompetitive(nums: number[], k: number): number[] {
    let stack = []
    for(let i = 0; i < nums.length; i++) {
        while(stack.length && nums[i] < stack[stack.length - 1] && stack.length - 1 + nums.length - i >= k) {
            stack.pop()
        }
        if(stack.length < k) {
            stack.push(nums[i])
        }
    }
    let result = Array(k).fill(0)
    for(let i = k - 1; i >= 0; i--) {
        result[i] = stack.pop()
    }
    return result
};
