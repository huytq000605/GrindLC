class NumMatrix {
    prefixSumMatrix
    constructor(matrix: number[][]) {
        this.prefixSumMatrix = Array(matrix.length).fill(0).map(() => Array(matrix[0].length))
        for(let row = 0; row < matrix.length; row++) {
            for(let col = 0; col < matrix[0].length; col++) {
                if(row === 0 && col === 0) {
                    this.prefixSumMatrix[0][0] = matrix[0][0]
                    continue
                }
                if(row === 0) {
                    this.prefixSumMatrix[0][col] = this.prefixSumMatrix[0][col - 1] + matrix[row][col]
                } else if(col === 0) {
                    this.prefixSumMatrix[row][0] = this.prefixSumMatrix[row - 1][0] + matrix[row][col]
                } else {
                    this.prefixSumMatrix[row][col] = this.prefixSumMatrix[row - 1][col] + this.prefixSumMatrix[row][col - 1] - this.prefixSumMatrix[row - 1][col - 1] + matrix[row][col]
                }
            }
        }
    }

    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        let top = 0
        let left = 0
        let cross = 0
        if(row1 !== 0) {
            top = this.prefixSumMatrix[row1 - 1][col2]
        }
        if(col1 !== 0) {
            left = this.prefixSumMatrix[row2][col1 - 1]
        }
        if(row1 !== 0 && col1 !== 0) {
            cross = this.prefixSumMatrix[row1 - 1][col1 - 1]
        }
        return this.prefixSumMatrix[row2][col2] - top - left + cross
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */