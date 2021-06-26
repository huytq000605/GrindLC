function findDiagonalOrder(mat: number[][]): number[] {
    let row = 0
    let col = 0
    let result = []
    let up = true
    while(result.length !== mat.length * mat[0].length) {
        if(row >= 0 && row < mat.length && col >= 0 && col < mat[0].length) { 
            result.push(mat[row][col])
        }
        if(up) {
            if(row === 0 || col === mat[0].length - 1) {
                col = col + 1
                up = false
            } else {
                row = row - 1
                col = col + 1
            }
        } else {
            if(col === 0 || row === mat.length - 1) {
                row = row + 1
                up = true
            } else {
                row = row + 1
                col = col - 1
            }
        }
    }
    return result
};