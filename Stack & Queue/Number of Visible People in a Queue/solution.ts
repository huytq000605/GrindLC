function canSeePersonsCount(heights: number[]): number[] {
    let result = Array(heights.length).fill(0)
    let stack = []
    for(let i = 0; i < heights.length; i++) {
        while(stack.length && heights[i] > heights[stack[stack.length - 1]]) {
            let idx = stack.pop()
            result[idx]++
        }
        if(stack.length) {
            result[stack[stack.length - 1]]++
        }
        stack.push(i)
    }
    return result
};