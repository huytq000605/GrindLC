function maxProductPath(grid: number[][]): number {
    let dpMax = Array(grid.length).fill(0).map(() => Array(grid[0].length))
    let dpMin = Array(grid.length).fill(0).map(() => Array(grid[0].length))
    dpMax[0][0] = grid[0][0]
    dpMin[0][0] = grid[0][0]
    for(let row = 1; row < grid.length; row++) { // Fill col 0
        dpMax[row][0] = dpMax[row - 1][0] * grid[row][0]
        dpMin[row][0] = dpMin[row-1][0] * grid[row][0]
    }
    for(let col = 1; col < grid[0].length; col++) { // Fill row 0
        dpMax[0][col] = dpMax[0][col-1] * grid[0][col]
        dpMin[0][col] = dpMin[0][col-1] * grid[0][col]
    }
    
    for(let i = 1; i < grid.length; i++) {
        for(let j = 1; j < grid[0].length; j++) {
            let max = Math.max(dpMax[i - 1][j], dpMax[i][j-1])
            let min = Math.min(dpMin[i - 1][j], dpMin[i][j-1])
            if(grid[i ][j ] < 0) {
                [max, min] = [min, max]
            }
            dpMax[i][j] = max * grid[i][j]
            dpMin[i][j] = min * grid[i][j]
        }
    }
    let result = dpMax[grid.length - 1][grid[0].length - 1]
    if(result < 0) return -1
    result = result % (1e9 + 7)
    return result
    
};