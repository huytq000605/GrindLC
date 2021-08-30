function searchMatrix(matrix: number[][], target: number): boolean {
    let min = 0
    let max = matrix.length - 1
    while(min < max) {
        let mid = min + Math.ceil((max - min + 1)/2)
        if(matrix[mid][0] === target) {
            return true
        } else if(matrix[mid][0] > target) {
            max = mid - 1
        } else {
            min = mid
        }
    }
    if(matrix[min][0] > target) return false
    let row = min
    min = 0
    max = matrix[0].length - 1
    while(min < max) {
        let mid = min + Math.floor((max - min) / 2)
        if(matrix[row][mid] === target) return true
        else if(matrix[row][mid] > target) {
            max = mid - 1
        } else {
            min = mid + 1
        }
    }
    if(matrix[row][min] === target) return true
    return false
};