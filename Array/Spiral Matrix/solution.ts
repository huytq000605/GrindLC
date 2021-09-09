function spiralOrder(matrix: number[][]): number[] {
    let minRow = 0
    let maxRow = matrix.length - 1
    let minCol = 0
    let maxCol = matrix[0].length - 1
    let num = matrix.length * matrix[0].length
    let result = []
    while(result.length < num) {
        for(let i = minCol; i <= maxCol; i++) {
            result.push(matrix[minRow][i])
        }
        if(result.length === num) return result
        for(let i = minRow + 1; i <= maxRow; i++) {
            result.push(matrix[i][maxCol])
        }
        if(result.length === num) return result
        for(let i = maxCol - 1; i >= minCol; i--) {
            result.push(matrix[maxRow][i])
        }
        for(let i = maxRow - 1; i > minRow; i--) {
            result.push(matrix[i][minRow])
        }
        minCol++
        maxCol--
        minRow++
        maxRow--
    }
    return result
};