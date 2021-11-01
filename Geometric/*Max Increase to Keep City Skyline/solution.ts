function maxIncreaseKeepingSkyline(grid: number[][]): number {
    let maxRow = Array(grid.length).fill(0)
    let maxCol = Array(grid[0].length).fill(0)
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            maxRow[i] = Math.max(maxRow[i], grid[i][j])
            maxCol[j] = Math.max(maxCol[j], grid[i][j])
        }
    }
    
    let result = 0
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            result += Math.min(maxRow[i], maxCol[j]) - grid[i][j]
        }
    }
    return result
};