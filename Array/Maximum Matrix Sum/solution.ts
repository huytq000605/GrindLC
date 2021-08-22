function maxMatrixSum(matrix: number[][]): number {
    let sum = 0
    let numOfNegative = 0
    let minAbs = Number.MAX_SAFE_INTEGER
    for(let row = 0; row < matrix.length; row++) {
        for(let col = 0; col < matrix.length; col++) {
            if(matrix[row][col] >= 0) {
                sum += matrix[row][col]
            } else {
                numOfNegative++
                sum += -matrix[row][col]
            }
            minAbs = Math.min(minAbs, Math.abs(matrix[row][col]))
        }
    }
    if(numOfNegative % 2 === 1) {
        sum -= 2 * minAbs
    }
    return sum
    
};