/**
 Do not return anything, modify matrix in-place instead.
 */
 function rotate(matrix: number[][]): void {
    for(let i = 0; i < matrix.length; i++) {
        for(let j = i; j < matrix[0].length; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        }
    }
    
    for(let row = 0; row < matrix.length; row++) { // Close wise, reverse each row
        for(let col = 0; col < matrix.length / 2; col++) {
            [matrix[row][col], matrix[row][matrix.length - col - 1]] = [matrix[row][matrix.length - col - 1], matrix[row][col]]
        }
    }

	// Anti clockwise, reverse each column
};