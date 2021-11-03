function mctFromLeafValues(arr: number[]): number {
    let stack = []
    let result = 0
    for(let i = 0; i < arr.length; i++) {
        while(stack.length && stack[stack.length - 1] < arr[i]) {
            let removed = stack.pop()
            let cost = Number.MAX_SAFE_INTEGER
            if(stack.length) cost = stack[stack.length - 1] * removed
            cost = Math.min(cost, arr[i] * removed)
            result += cost
        }
        stack.push(arr[i])
    }
    
    while(stack.length >= 2) {
        result += stack.pop() * stack[stack.length - 1]
    }
    return result
};