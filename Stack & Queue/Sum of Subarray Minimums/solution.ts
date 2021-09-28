function sumSubarrayMins(arr: number[]): number {
    let nextSmallerElement = Array(arr.length).fill(arr.length)
    let prevSmallerElement = Array(arr.length).fill(-1)
    let stack = []
    
    for(let i = 0; i < arr.length; i++) {
        while(stack.length && arr[i] <= arr[stack[stack.length - 1]]) {
            nextSmallerElement[stack.pop()] = i
        }
        stack.push(i)
    }
    
    stack = []
    for(let i = arr.length - 1; i >= 0; i--) {
        while(stack.length && arr[i] < arr[stack[stack.length -1]]) {
            prevSmallerElement[stack.pop()] = i
        }
        stack.push(i)
    }
    let result = 0
    for(let i = 0; i < arr.length; i++) {
        let nextSmaller = nextSmallerElement[i]
        let prevSmaller = prevSmallerElement[i]
        let endPoint = nextSmaller - 1
        let startPoint = prevSmaller + 1
        result += (endPoint - i + 1) * (i - startPoint + 1) * arr[i]
        result = result % (1e9 + 7)
    }
    return result
};