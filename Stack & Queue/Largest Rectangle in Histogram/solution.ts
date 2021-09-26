function largestRectangleArea(heights: number[]): number {
    let nextSmaller = Array(heights.length).fill(heights.length)
    let prevSmaller = Array(heights.length).fill(-1)
    let stack = []
    for(let i = 0; i < heights.length; i++) {
        while(stack.length && heights[i] < heights[stack[stack.length - 1]]) {
            nextSmaller[stack.pop()] = i
        }
        stack.push(i)
    }
    
    stack = []
    for(let i = heights.length - 1; i >= 0; i--) {
        while(stack.length && heights[i] < heights[stack[stack.length - 1]]) {
            prevSmaller[stack.pop()] = i
        }
        stack.push(i)
    }
    
    let result = 0
    for(let i = 0; i < heights.length; i++) {
        let min = heights[i]
        let next = nextSmaller[i]
        let prev = prevSmaller[i]
        result = Math.max(result, ((next - 1) - (prev + 1) + 1) * min)
    }
    return result
};