function maxSumMinProduct(nums: number[]): number {
    let prefix = Array(nums.length)
    prefix[0] = BigInt(nums[0])
    for(let i = 1; i < nums.length; i++) {
        prefix[i] = prefix[i-1] + BigInt(nums[i])
    }
    let nextSmallerElement = Array(nums.length).fill(nums.length)
    let prevSmallerElement = Array(nums.length).fill(-1)
    let stack = []
    for(let i = 0; i < nums.length; i++) {
        while(stack.length && nums[i] < nums[stack[stack.length -1]]) {
            nextSmallerElement[stack.pop()] = i
        }
        stack.push(i)
    }
    
    stack = []
    for(let i = nums.length - 1; i >= 0; i--) {
        while(stack.length && nums[i] < nums[stack[stack.length - 1]]) {
            prevSmallerElement[stack.pop()] = i
        }
        stack.push(i)
    }
    let result = 0n
    for(let i = 0; i < nums.length; i++) {
        let leftRange = prevSmallerElement[i]
        let rightRange = nextSmallerElement[i]
        let sum
        if(leftRange === -1) {
            sum = prefix[rightRange-1]
        } else {
            sum = prefix[rightRange-1] - prefix[leftRange]
        }
        let res = sum * BigInt(nums[i])
        if(res > result) {
            result = res
        }   
    }
    result = result % BigInt(1e9 + 7)
    return Number(result)
    
};