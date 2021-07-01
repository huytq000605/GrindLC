function cherryPickup(grid: number[][]): number {
    let cache = new Map()
    return dfs(grid, 0, 0, grid[0].length - 1, cache)
};

function dfs(grid: number[][], row: number, col1: number, col2: number, cache: Map<string, number>) {
    if(row >= grid.length || col1 < 0 || col1 >= grid[0].length || col2 < 0 || col2 >= grid[0].length) {
        return 0
    }
    const key = `${row}-${col1}-${row}-${col2}`
    if(cache.has(key)) {
        return cache.get(key)
    }
    let thisRow = 0;
    if(col1 === col2) {
        thisRow += grid[row][col1]
    } else {
        thisRow += grid[row][col1] + grid[row][col2]
    }
    let belowThisRow = 0
    for(let i = -1; i <= 1; i++) {
        for(let j = -1; j <= 1; j++) {
            belowThisRow = Math.max(belowThisRow, dfs(grid, row + 1, col1 + i, col2 +j, cache))
        }
    }
    cache.set(key, thisRow  + belowThisRow)
    return thisRow + belowThisRow
}