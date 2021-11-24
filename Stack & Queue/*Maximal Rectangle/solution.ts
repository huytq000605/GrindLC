function maximalRectangle(matrix: string[][]): number {
    if(!matrix.length) return 0
    let result = 0
    let height = Array(matrix[0].length).fill(0)
    for(let row = 0; row < matrix.length; row++) {
        for(let col = 0; col < matrix[0].length; col++) {
            if(matrix[row][col] === "1") {
                height[col] += 1
            } else {
                height[col] = 0
            }
        }
        
        let nextSmaller = Array(matrix[0].length).fill(matrix[0].length)
        let prevSmaller = Array(matrix[0].length).fill(-1)
        
        let stack = []
        for(let col = 0; col < matrix[0].length; col++) {
            while(stack.length && height[col] < height[stack[stack.length - 1]]) {
                nextSmaller[stack.pop()] = col
            }
            stack.push(col)
        }
        
        stack = []
        for(let col = matrix[0].length - 1; col >= 0; col--) {
            while(stack.length && height[col] < height[stack[stack.length - 1]]) {
                prevSmaller[stack.pop()] = col
            }
            stack.push(col)
        }
        
        for(let col = 0; col < matrix[0].length; col++) {
            result = Math.max(result, ((nextSmaller[col] - 1) - (prevSmaller[col] + 1) + 1) * height[col])
        }
    }
    return result
};