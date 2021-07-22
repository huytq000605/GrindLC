function searchMatrix(matrix: number[][], target: number): boolean {
    let minCol = 0
    let maxRow = matrix.length - 1
    while(maxRow >= 0 && minCol <= matrix[0].length - 1) {
        if(target < matrix[maxRow][minCol]) {
            maxRow--
            continue
        }
        if(target > matrix[maxRow][minCol]) {
            minCol++
            continue
        }
        if(target === matrix[maxRow][minCol]) {
            return true
        }
        
    }
    return false
};