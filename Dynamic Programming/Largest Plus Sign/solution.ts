function orderOfLargestPlusSign(n: number, mines: number[][]): number {
    let matrix = Array(n).fill(0).map(() => Array(n).fill(1))
    for(let mine of mines) {
        matrix[mine[0]][mine[1]] = 0
    }
    let up = Array(n).fill(0).map(() => Array(n).fill(1))
    let down = Array(n).fill(0).map(() => Array(n).fill(1))
    let left = Array(n).fill(0).map(() => Array(n).fill(1))
    let right = Array(n).fill(0).map(() => Array(n).fill(1))
    
    for(let row = 0; row < n; row++) {
        for(let col = 0; col < n; col++) {
            if(matrix[row][col] === 0) {
                up[row][col] = 0
                down[row][col] = 0
                left[row][col] = 0
                right[row][col] = 0
            } else {
                if(row > 0) up[row][col] = up[row - 1][col] + 1
                if(col > 0) left[row][col] = left[row][col - 1] + 1
            }
        }
    }
    
    for(let row = n - 1; row >= 0; row--) {
        for(let col = n - 1; col >= 0; col--) {
            if(matrix[row][col] === 1) {
                if(row < n-1) down[row][col] = down[row + 1][col] + 1
                if(col < n-1) right[row][col] = right[row][col + 1] + 1
            }
        }
    }
    let result = 0
    
    for(let row = 0; row < n; row++) {
        for(let col = 0; col < n; col++) {
            result = Math.max(result, Math.min(up[row][col], down[row][col], right[row][col], left[row][col]))
        }
    }
    
    return result

};